# oscars_all_nominees_by_category_FILM_ONLY_ENHANCED.py
# Enhanced version with improved parsing for early years (1929-1934)
# Scrape Oscars Winners & Nominees (1929–2025), write ONE CSV PER CATEGORY with FILM-ONLY rows.
# Using Bright Data Browser API WebDriver protocol to bypass anti-scraping measures

import argparse
import csv
import re
import sys
import time
import random
import json
import os
from pathlib import Path
import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Import enhanced parsing functions
from enhanced_parsing import (
    enhanced_extract_wn_lines,
    enhanced_parse_winners_nominees,
    enhanced_looks_like_category_heading
)

# Bright Data Browser API configuration from environment variables
BRIGHT_DATA_USERNAME = os.getenv('BRIGHT_DATA_USERNAME')
BRIGHT_DATA_PASSWORD = os.getenv('BRIGHT_DATA_PASSWORD')
BRIGHT_DATA_HOST = os.getenv('BRIGHT_DATA_HOST', 'brd.superproxy.io')
BRIGHT_DATA_PORT = os.getenv('BRIGHT_DATA_PORT', '9515')

if not BRIGHT_DATA_USERNAME or not BRIGHT_DATA_PASSWORD:
    raise ValueError("Missing Bright Data credentials. Please set BRIGHT_DATA_USERNAME and BRIGHT_DATA_PASSWORD in your .env file")

BRIGHT_DATA_BASE = f"https://{BRIGHT_DATA_USERNAME}:{BRIGHT_DATA_PASSWORD}@{BRIGHT_DATA_HOST}:{BRIGHT_DATA_PORT}"

DEFAULT_START = 1929
DEFAULT_END = 2025
BASE = "https://www.oscars.org/oscars/ceremonies/{year}"
OUTDIR = Path("data/oscars_nominees_by_category_FILMS_ENHANCED")
CACHE_DIR = Path("data/html_cache")

# Import historical category mapping
from oscar_categories_historical import (
    get_categories_for_year, 
    normalize_category, 
    get_all_known_categories,
    get_modern_categories
)

def get_cache_path(year: int) -> Path:
    """Get the cache file path for a given year."""
    return CACHE_DIR / f"oscar_{year}.html"

def load_cached_html(year: int) -> str:
    """Load HTML from cache if available."""
    cache_file = get_cache_path(year)
    if cache_file.exists():
        print(f"  Loading cached HTML for {year}")
        try:
            with open(cache_file, 'r', encoding='utf-8') as f:
                return f.read()
        except Exception as e:
            print(f"  Warning: Failed to read cache file {cache_file}: {e}")
            return None
    return None

def save_html_to_cache(year: int, html_content: str) -> bool:
    """Save HTML content to cache."""
    try:
        # Ensure cache directory exists
        CACHE_DIR.mkdir(parents=True, exist_ok=True)
        
        cache_file = get_cache_path(year)
        with open(cache_file, 'w', encoding='utf-8') as f:
            f.write(html_content)
        
        print(f"  Cached HTML for {year} to {cache_file}")
        return True
    except Exception as e:
        print(f"  Warning: Failed to cache HTML for {year}: {e}")
        return False

def fetch_html_cached(year: int, use_cache: bool = True, refresh_cache: bool = False) -> tuple[str, str]:
    """
    Fetch HTML with caching support.
    
    Args:
        year: Year to fetch
        use_cache: Whether to use cached version if available
        refresh_cache: Whether to refresh the cache (re-download even if cached)
    
    Returns:
        tuple of (html_content, source_url)
    """
    source_url = BASE.format(year=year)
    
    # Try to load from cache first (unless refresh is requested)
    if use_cache and not refresh_cache:
        cached_html = load_cached_html(year)
        if cached_html:
            return cached_html, source_url
    
    # Cache miss or refresh requested - fetch from web
    print(f"  Fetching HTML from web for {year}")
    
    # Create session and fetch
    session_id = create_browser_session()
    if not session_id:
        print(f"  Failed to create Bright Data session for {year}")
        return None, source_url
    
    try:
        soup, _ = fetch_html_with_brightdata(year, session_id)
        if soup:
            # Convert BeautifulSoup to string for caching
            html_content = str(soup)
            # Save to cache
            save_html_to_cache(year, html_content)
            return html_content, source_url
        else:
            print(f"  Failed to fetch HTML for {year}")
            return None, source_url
    finally:
        # Always clean up the session
        delete_browser_session(session_id)

def norm(s: str) -> str:
    return re.sub(r"\s+", " ", (s or "").strip())

def slugify(name: str) -> str:
    s = name.strip()
    s = s.replace("&", "and")
    s = re.sub(r"[^\w\s\-\(\)]", "", s)
    s = re.sub(r"[\s/]+", "_", s)
    return s

def create_browser_session():
    """Create a new browser session using Bright Data WebDriver API."""
    session_payload = {
        "capabilities": {
            "browserName": "chrome",
            "platformName": "windows"
        }
    }
    
    response = requests.post(f"{BRIGHT_DATA_BASE}/session", json=session_payload, timeout=60)
    
    if response.status_code != 200:
        raise Exception(f"Failed to create session: HTTP {response.status_code} - {response.text}")
    
    session_data = response.json()
    return session_data["value"]["sessionId"]

def delete_browser_session(session_id):
    """Delete a browser session."""
    try:
        response = requests.delete(f"{BRIGHT_DATA_BASE}/session/{session_id}", timeout=60)
        if response.status_code == 200:
            print(f"    Session {session_id} deleted successfully")
        else:
            print(f"    Warning: Failed to delete session {session_id}")
    except Exception as e:
        print(f"    Warning: Error deleting session {session_id}: {e}")

def fetch_html_with_brightdata(year: int, session_id: str, max_retries=3):
    """Fetch HTML using Bright Data Browser API WebDriver protocol."""
    target_url = BASE.format(year=year)
    
    for attempt in range(max_retries):
        try:
            print(f"  Attempt {attempt + 1}: Fetching {target_url}")
            
            # Add random delay to appear more human-like
            time.sleep(random.uniform(2.0, 5.0))
            
            # Navigate to the target URL
            navigate_payload = {"url": target_url}
            response = requests.post(f"{BRIGHT_DATA_BASE}/session/{session_id}/url", json=navigate_payload, timeout=60)
            
            if response.status_code != 200:
                print(f"    HTTP {response.status_code}: {response.text}")
                if attempt < max_retries - 1:
                    time.sleep(random.uniform(10.0, 25.0))
                    continue
                return None, None
            
            # Wait for page to load
            time.sleep(3)
            
            # Get page source
            response = requests.get(f"{BRIGHT_DATA_BASE}/session/{session_id}/source", timeout=60)
            
            if response.status_code == 200:
                source_data = response.json()
                html_content = source_data["value"]
                soup = BeautifulSoup(html_content, "html.parser")
                
                # Check if page loaded successfully
                title = soup.find('title')
                if title and ("404" in title.get_text().lower() or "not found" in title.get_text().lower()):
                    print(f"    404 - Year {year} not available")
                    return None, None
                
                if title and ("403" in title.get_text().lower() or "forbidden" in title.get_text().lower()):
                    print(f"    403 Forbidden - retrying...")
                    time.sleep(random.uniform(10.0, 20.0))
                    continue
                
                print(f"    Successfully loaded page: {title.get_text() if title else 'No title'}")
                return soup, target_url
                
            else:
                print(f"    HTTP {response.status_code}: {response.text}")
                if attempt < max_retries - 1:
                    time.sleep(random.uniform(10.0, 25.0))
                    continue
                
        except requests.exceptions.RequestException as e:
            print(f"    Error on attempt {attempt + 1}: {e}")
            if attempt < max_retries - 1:
                time.sleep(random.uniform(10.0, 25.0))
            else:
                print(f"    Failed to fetch {target_url} after {max_retries} attempts")
                return None, None
    
    return None, None

def write_by_category(rows, outdir: Path):
    # Ensure the directory and all parent directories exist
    outdir.mkdir(parents=True, exist_ok=True)
    
    by_cat = {}
    for r in rows:
        by_cat.setdefault(r["category"], []).append(r)

    for cat, items in by_cat.items():
        path = outdir / f"{slugify(cat)}.csv"
        write_header = not path.exists()
        items_sorted = sorted(items, key=lambda x: (x["ceremony_year"], not x["is_winner"], x["film"]))
        with path.open("a", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(f, fieldnames=["ceremony_year", "category", "film", "is_winner", "source_url"])
            if write_header:
                w.writeheader()
            for row in items_sorted:
                w.writerow(row)

def run(start_year: int, end_year: int, delay: float, use_cache: bool = True, refresh_cache: bool = False):
    """Main scraping function using enhanced parsing logic."""
    print("Using Enhanced Oscar Scraping with Improved Early Years Parsing...")
    
    print(f"Cache enabled: {use_cache}, Refresh cache: {refresh_cache}")
    print(f"Cache directory: {CACHE_DIR}")
    
    try:
        all_rows = []
        for year in range(start_year, end_year + 1):
            try:
                print(f"\nProcessing year {year}...")
                # Use cached fetch
                html_content, url = fetch_html_cached(year, use_cache=use_cache, refresh_cache=refresh_cache)
                
                if html_content is None:
                    print(f"[warn] {year}: Could not fetch or load HTML", file=sys.stderr)
                    continue
                
                soup = BeautifulSoup(html_content, "html.parser")
                
                # Use enhanced extraction with year-specific logic
                lines = enhanced_extract_wn_lines(soup, year)
                if not lines:
                    print(f"[warn] {year}: Could not find 'Winners & Nominees' block", file=sys.stderr)
                    continue
                
                # Use enhanced parsing with year-specific logic
                rows = enhanced_parse_winners_nominees(lines, year, url)
                if not rows:
                    print(f"[warn] {year}: No rows parsed", file=sys.stderr)
                else:
                    print(f"[ok] {year}: {len(rows)} rows")
                    all_rows.extend(rows)
                
                time.sleep(delay)
                
            except Exception as e:
                print(f"[warn] {year}: {e}", file=sys.stderr)
                continue

        write_by_category(all_rows, OUTDIR)
        print(f"\nDone. Wrote enhanced film-only CSVs to: {OUTDIR.resolve()}")
        print("Examples you should see:")
        for ex in ("Best_Picture.csv", "Actor_in_a_Leading_Role.csv",
                   "Writing_Original_Screenplay.csv", "Music_Original_Song.csv"):
            print(" -", (OUTDIR / ex))
            
    finally:
        # Cleanup happens in fetch_html_cached for each request
        pass

if __name__ == "__main__":
    ap = argparse.ArgumentParser(description="Enhanced Oscar scraping with improved early years parsing using Bright Data Browser API WebDriver protocol.")
    ap.add_argument("--start", type=int, default=DEFAULT_START, help="Start ceremony year (e.g., 1929)")
    ap.add_argument("--end", type=int, default=DEFAULT_END, help="End ceremony year (e.g., 2025)")
    ap.add_argument("--delay", type=float, default=2.0, help="Seconds between requests (be polite)")
    ap.add_argument("--no-cache", action="store_true", help="Disable HTML caching (always fetch from web)")
    ap.add_argument("--refresh-cache", action="store_true", help="Refresh cached HTML (re-download even if cached)")
    ap.add_argument("--cache-dir", type=str, default=str(CACHE_DIR), help="Directory for HTML cache files")
    args = ap.parse_args()
    
    # Update cache directory if specified
    if args.cache_dir != str(CACHE_DIR):
        CACHE_DIR = Path(args.cache_dir)
    
    run(args.start, args.end, args.delay, 
        use_cache=not args.no_cache, 
        refresh_cache=args.refresh_cache)


