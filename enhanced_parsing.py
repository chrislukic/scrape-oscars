#!/usr/bin/env python3
"""
Enhanced parsing logic for Oscar awards with year-specific improvements.
Addresses issues with early years (1929-1934) and improves category detection.
"""

import re
from typing import List, Dict, Tuple, Optional
from bs4 import BeautifulSoup

def norm(s: str) -> str:
    """Normalize string by removing extra whitespace."""
    return re.sub(r"\s+", " ", (s or "").strip())

def lower_norm(s: str) -> str:
    """Normalize and lowercase string."""
    return norm(s).lower()

# Enhanced category keywords for better detection
ENHANCED_CATEGORY_KEYWORDS = {
    "picture", "role", "directing", "writing", "music", "cinematography", 
    "editing", "design", "effects", "sound", "makeup", "costume", 
    "animated", "documentary", "short", "international", "foreign", 
    "feature", "film", "score", "song", "screenplay", "adapted", 
    "original", "supporting", "leading", "actress", "actor", "production",
    "art", "direction", "story", "title", "comedy", "dramatic", "assistant"
}

# Early years specific patterns (1929-1934)
EARLY_YEARS_CATEGORY_PATTERNS = [
    r"^(Outstanding|Best)\s+(Picture|Production|Actor|Actress|Director|Writing)",
    r"^(Best|Outstanding)\s+[A-Z][a-zA-Z\s\(\),-]+$",
    r"^[A-Z][a-z\s]+(?:\([^)]+\))?$",  # "Actor in a Leading Role"
    r"^[A-Z][a-z\s]+(?:\([^)]+\))?\s*$",  # With trailing spaces
]

# Modern years patterns (1935+)
MODERN_YEARS_CATEGORY_PATTERNS = [
    r"^(Best|Outstanding)\s+[A-Z][a-zA-Z\s\(\),-]+$",
    r"^[A-Z][a-z\s]+(?:\([^)]+\))?$",
    r"^[A-Z][a-z\s]+(?:\([^)]+\))?\s*$",
]

# Common actor/actress names that should not be treated as categories
COMMON_ACTOR_NAMES = {
    "mary pickford", "warner baxter", "george arliss", "norma shearer",
    "fredric march", "helen hayes", "wallace beery", "charles laughton",
    "katharine hepburn", "leslie howard", "paul muni", "marie dressler",
    "lionel barrymore", "adolphe menjou", "ann harding", "irene dunne",
    "jackie cooper", "marlene dietrich", "richard dix", "norma shearer",
    "george bancroft", "bessie love", "betty compson", "chester morris",
    "corinne griffith", "jeanne eagels", "lewis stone", "ruth chatterton"
}

# Common film titles that might be mistaken for categories
COMMON_FILM_TITLES = {
    "sunrise", "wings", "the jazz singer", "the circus", "7th heaven",
    "the crowd", "the racket", "chang", "the broadway melody",
    "the bridge of san luis rey", "the patriot", "white shadows in the south seas",
    "all quiet on the western front", "cimarron", "grand hotel"
}

def is_early_years_format(year: int) -> bool:
    """Determine if this is an early years format (1929-1934)."""
    return 1929 <= year <= 1934

def is_likely_actor_name(text: str) -> bool:
    """Check if text is likely an actor/actress name."""
    text_lower = lower_norm(text)
    
    # Check against known actor names
    if text_lower in COMMON_ACTOR_NAMES:
        return True
    
    # Don't treat category names as actor names
    if text_lower.startswith(('best ', 'outstanding ')):
        return False
    
    # Don't treat single category words as actor names
    if text_lower in ['actor', 'actress', 'director', 'cinematography', 'direction', 'writing', 'effects', 'engineering', 'art direction']:
        return False
    
    # Check for common actor name patterns
    words = text.split()
    if len(words) == 2:
        # Two-word names like "Mary Pickford"
        if all(word[0].isupper() for word in words):
            return True
    
    # Check for single names that are likely actors
    if len(words) == 1 and text[0].isupper():
        # Single capitalized word - could be actor name
        return True
    
    return False

def is_likely_film_title(text: str) -> bool:
    """Check if text is likely a film title."""
    text_lower = lower_norm(text)
    
    # Don't treat category names as film titles
    if text_lower.startswith(('best ', 'outstanding ')):
        return False
    
    # Don't treat category words as film titles
    if text_lower in ['actor', 'actress', 'director', 'cinematography', 'direction', 'writing', 'effects', 'engineering', 'art direction']:
        return False
    
    # Check against known film titles
    if text_lower in COMMON_FILM_TITLES:
        return True
    
    # Check for film title patterns
    words = text.split()
    
    # Single word titles
    if len(words) == 1 and text[0].isupper():
        return True
    
    # Multi-word titles with proper capitalization
    if len(words) >= 2:
        # Check if first word is capitalized and others might be
        if words[0][0].isupper():
            return True
    
    return False

def enhanced_looks_like_category_heading(s: str, year: int) -> bool:
    """
    Enhanced category heading detection with year-specific logic.
    """
    ls = lower_norm(s)
    s_clean = s.strip()
    
    # Basic length checks
    if len(s_clean) < 4 or len(s_clean) > 70:
        return False
    
    # Exclude common fragments
    exclude_fragments = {
        "view by category", "view by film", "select a category",
        "highlights", "memorable moments", "share", "winner", "nominees", "nominee"
    }
    if any(x in ls for x in exclude_fragments):
        return False
    
    # Check if it's likely an actor name or film title first
    if is_likely_actor_name(s_clean) or is_likely_film_title(s_clean):
        return False
    
    # For early years (1929-1934), get the valid categories for this year
    from oscar_categories_historical import get_categories_for_year
    valid_categories = get_categories_for_year(year)
    
    # Check exact match with valid categories (full names)
    if s_clean in valid_categories:
        return True
    
    # Check simplified versions (without "Best" prefix)
    for cat in valid_categories:
        # Remove "Best " prefix for comparison
        simplified = cat.replace("Best ", "").replace("Outstanding ", "")
        if s_clean == simplified:
            return True
        
        # Handle special cases like "Directing (Comedy Picture)"
        if "directing" in simplified.lower() and "directing" in ls:
            return True
    
    # Check traditional patterns for categories that start with Best/Outstanding
    if re.match(r"^(Best|Outstanding)\s+[A-Z]", s_clean):
        return True
    
    # Check for specific category keywords that indicate this is a category
    category_indicators = {
        "actor", "actress", "director", "directing", "writing", "cinematography",
        "art direction", "production design", "sound", "music", "editing",
        "effects", "engineering", "costume", "makeup", "documentary", "short",
        "animated", "foreign", "international", "picture", "production"
    }
    
    # Check if it contains category indicators and has proper structure
    if any(indicator in ls for indicator in category_indicators):
        # Must start with capital letter and have proper capitalization
        if re.match(r"^[A-Z][a-zA-Z\s\(\),-]+$", s_clean):
            # Additional check: shouldn't be too short for complex categories
            if len(s_clean) >= 4:
                return True
    
    return False

def enhanced_early_years_category_detection(s: str, year: int) -> bool:
    """Enhanced category detection for early years (1929-1934)."""
    ls = lower_norm(s)
    
    # Check for early years specific patterns
    for pattern in EARLY_YEARS_CATEGORY_PATTERNS:
        if re.match(pattern, s):
            # Additional validation for early years
            if is_likely_actor_name(s):
                return False
            
            if is_likely_film_title(s):
                return False
            
            # Check for category keywords
            if any(keyword in ls for keyword in ENHANCED_CATEGORY_KEYWORDS):
                return True
            
            # Special handling for early years categories
            if any(prefix in ls for prefix in ["outstanding", "best"]):
                return True
    
    # Additional check: if it starts with "Best" or "Outstanding" and has proper capitalization
    if re.match(r"^(Best|Outstanding)\s+[A-Z]", s):
        if not is_likely_actor_name(s) and not is_likely_film_title(s):
            return True
    
    return False

def enhanced_modern_years_category_detection(s: str, year: int) -> bool:
    """Enhanced category detection for modern years (1935+)."""
    ls = lower_norm(s)
    
    # Check for modern patterns
    for pattern in MODERN_YEARS_CATEGORY_PATTERNS:
        if re.match(pattern, s):
            # Additional validation
            if is_likely_actor_name(s):
                return False
            
            if is_likely_film_title(s):
                return False
            
            # Check for category keywords
            if any(keyword in ls for keyword in ENHANCED_CATEGORY_KEYWORDS):
                return True
    
    # Additional check: if it starts with "Best" and has proper capitalization
    if re.match(r"^Best\s+[A-Z]", s):
        if not is_likely_actor_name(s) and not is_likely_film_title(s):
            return True
    
    return False

def enhanced_extract_wn_lines(soup: BeautifulSoup, year: int) -> List[str]:
    """
    Enhanced extraction of Winners & Nominees lines with year-specific logic.
    """
    lines = list(soup.stripped_strings)
    out, in_section = [], False
    
    for s in lines:
        s_clean = norm(s)
        up = s_clean.upper()
        
        if not in_section:
            if up.startswith("WINNERS & NOMINEES"):
                in_section = True
            continue
        
        # Early years might have different section endings
        if is_early_years_format(year):
            # Early years might not have the "0-9 ALL" pattern
            if ("0-9" in s_clean and "ALL" in s_clean) or s_clean == "0-9":
                break
            # Be more specific about section end markers to avoid stopping on navigation elements
            if up.startswith("VIEW BY FILM") or up.startswith("VIEW BY CATEGORY"):
                # Skip navigation elements but don't break
                continue
            # More specific end markers
            if up.startswith("ALPHABETICAL") or up.startswith("INDEX"):
                break
        else:
            # Modern years use the standard pattern
            if ("0-9" in s_clean and "ALL" in s_clean) or s_clean == "0-9":
                break
        
        out.append(s_clean)
    
    return out

def enhanced_consume_entry(lines: List[str], start_idx: int, year: int, max_lines: int = 2) -> Tuple[str, int]:
    """
    Enhanced entry consumption with year-specific logic.
    """
    entry_parts, i, n = [], start_idx + 1, len(lines)
    
    while i < n:
        t = norm(lines[i])
        low = t.lower()
        
        if not t:
            i += 1
            continue
        
        if low in ("winner", "nominee", "nominees"):
            if entry_parts:
                break
            i += 1
            continue
        
        # Use year-specific category detection
        if enhanced_looks_like_category_heading(t, year) and entry_parts:
            break
        
        entry_parts.append(t)
        if len(entry_parts) >= max_lines:
            break
        i += 1
    
    return (" — ".join(entry_parts).strip(" —"), i)

def enhanced_extract_film_only(category_canon: str, entry: str, year: int) -> str:
    """
    Enhanced film extraction with year-specific logic.
    """
    # normalize dashes
    s = norm(entry)
    parts = re.split(r"\s[—–-]\s", s)
    cl = category_canon.lower()

    # Early years might have different formatting
    if is_early_years_format(year):
        return enhanced_early_years_film_extraction(category_canon, entry, parts)
    
    # Modern years logic
    if use_right_side_for_film(category_canon):
        if "original song" in cl and len(parts) >= 2:
            # Song — Film — (Credits)
            film = parts[1] if len(parts) >= 2 else parts[-1]
        else:
            film = parts[-1] if parts else s
    else:
        film = parts[0] if parts else s

    # Cleanup
    film = film.strip(" '\"\"")
    film = re.sub(r'^from\s+', '', film, flags=re.IGNORECASE)
    film = re.sub(r';\s*.*$', '', film)
    film = film.strip()
    
    return film

def enhanced_early_years_film_extraction(category_canon: str, entry: str, parts: List[str]) -> str:
    """
    Enhanced film extraction specifically for early years.
    """
    s = norm(entry)
    cl = category_canon.lower()
    
    # Early years often have simpler formatting
    if len(parts) == 1:
        # Single part - likely just the film title
        film = parts[0]
    elif len(parts) >= 2:
        # Multiple parts - need to determine which is the film
        if "actor" in cl or "actress" in cl:
            # For acting categories, film is usually on the right
            film = parts[-1]
        else:
            # For other categories, film is usually on the left
            film = parts[0]
    else:
        film = s
    
    # Cleanup
    film = film.strip(" '\"\"")
    film = re.sub(r'^from\s+', '', film, flags=re.IGNORECASE)
    film = re.sub(r';\s*.*$', '', film)
    film = film.strip()
    
    return film

def use_right_side_for_film(category_canon: str) -> bool:
    """Categories where the film typically appears on the RIGHT."""
    cl = category_canon.lower()
    if "original song" in cl:
        return True
    if "actor" in cl or "actress" in cl:
        return True
    return False

def enhanced_parse_winners_nominees(lines: List[str], year: int, source_url: str) -> List[Dict]:
    """
    Enhanced parsing with year-specific logic.
    """
    rows = []
    current_category_raw = None

    i, n = 0, len(lines)
    while i < n:
        t = norm(lines[i])
        low = t.lower()
        
        # Use enhanced category detection
        if enhanced_looks_like_category_heading(t, year):
            current_category_raw = t
            i += 1
            continue

        if low == "winner":
            if current_category_raw is None:
                # Look back for category heading with enhanced detection
                for j in range(i - 1, max(-1, i - 15), -1):
                    cand = norm(lines[j])
                    if enhanced_looks_like_category_heading(cand, year):
                        current_category_raw = cand
                        break
            
            # Import the to_canonical function from the main module
            from oscar_categories_historical import normalize_category, get_categories_for_year
            
            # Map simplified category names to full category names
            category_raw = current_category_raw or "Unknown Category"
            valid_categories = get_categories_for_year(year)
            
            # Try to find the full category name
            full_category_name = category_raw
            for valid_cat in valid_categories:
                simplified = valid_cat.replace("Best ", "").replace("Outstanding ", "")
                if category_raw == simplified:
                    full_category_name = valid_cat
                    break
            
            category = normalize_category(full_category_name, year)
            entry, next_i = enhanced_consume_entry(lines, i, year, max_lines=2)
            
            if entry:
                film = enhanced_extract_film_only(category, entry, year)
                rows.append({
                    "ceremony_year": year,
                    "category": category,
                    "film": film,
                    "is_winner": True,
                    "source_url": source_url,
                })
            i = next_i
            continue

        if low in ("nominee", "nominees"):
            if current_category_raw is None:
                # Look back for category heading with enhanced detection
                for j in range(i - 1, max(-1, i - 15), -1):
                    cand = norm(lines[j])
                    if enhanced_looks_like_category_heading(cand, year):
                        current_category_raw = cand
                        break
            
            # Import the to_canonical function from the main module
            from oscar_categories_historical import normalize_category, get_categories_for_year
            
            # Map simplified category names to full category names
            category_raw = current_category_raw or "Unknown Category"
            valid_categories = get_categories_for_year(year)
            
            # Try to find the full category name
            full_category_name = category_raw
            for valid_cat in valid_categories:
                simplified = valid_cat.replace("Best ", "").replace("Outstanding ", "")
                if category_raw == simplified:
                    full_category_name = valid_cat
                    break
            
            category = normalize_category(full_category_name, year)
            entry, next_i = enhanced_consume_entry(lines, i, year, max_lines=2)
            
            if entry:
                film = enhanced_extract_film_only(category, entry, year)
                rows.append({
                    "ceremony_year": year,
                    "category": category,
                    "film": film,
                    "is_winner": False,
                    "source_url": source_url,
                })
            i = next_i
            continue

        i += 1

    # De-dup within a (year, category, film) triple (winner beats nominee if both appear)
    dedup = {}
    for r in rows:
        key = (r["ceremony_year"], r["category"], r["film"])
        cur = dedup.get(key)
        if cur is None or (r["is_winner"] and not cur["is_winner"]):
            dedup[key] = r
    
    return list(dedup.values())
