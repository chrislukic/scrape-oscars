# Oscars Scraper

A Python script to scrape Oscar winners and nominees from the official Academy Awards website and generate CSV files organized by category. Uses Bright Data's Browser API to bypass anti-scraping measures.

## Overview

This tool scrapes the Oscars website (oscars.org) to collect data about winners and nominees from 1929-2025. It generates separate CSV files for each award category, containing only film titles (not individual credits like actors, directors, etc.). The script uses Bright Data's Browser API to bypass aggressive anti-scraping measures.

## Features

- Scrapes Oscar ceremony data from 1929 to 2025
- Generates one CSV file per award category
- Extracts film titles only (filters out individual credits)
- Handles category name normalization and canonicalization
- Includes source URLs for data verification
- Respectful scraping with configurable delays
- Uses Bright Data Browser API to bypass anti-scraping measures
- Supports historical category evolution over time

## Installation

1. Clone this repository:
```bash
git clone <repository-url>
cd scrape-oscars
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set up your Bright Data credentials:
```bash
# Copy the example environment file
cp .env.example .env

# Edit .env with your actual Bright Data credentials
# Get these from your Bright Data Browser API endpoint
```

## Bright Data Setup

1. Create a Bright Data account at https://brightdata.com/
2. Set up a Browser API zone
3. Copy your endpoint credentials to the `.env` file:
   ```
   BRIGHT_DATA_USERNAME=your_username_from_bright_data
   BRIGHT_DATA_PASSWORD=your_password_from_bright_data
   BRIGHT_DATA_HOST=brd.superproxy.io
   BRIGHT_DATA_PORT=9515
   ```

## Usage

### Basic Usage

Run the enhanced script with default settings (1929-2025):
```bash
python scrape-oscars-enhanced.py
```

### Custom Year Range

Specify a custom year range:
```bash
python scrape-oscars-enhanced.py --start 2010 --end 2020
```

### Adjust Request Delay

Modify the delay between requests (default: 2.0 seconds):
```bash
python scrape-oscars-enhanced.py --delay 3.0
```

### Command Line Options

- `--start`: Start year (default: 1929)
- `--end`: End year (default: 2025)
- `--delay`: Delay between requests in seconds (default: 2.0)

### Testing

Test the enhanced parsing logic:
```bash
python test_enhanced_parsing.py
```

## Output

The enhanced script creates a directory called `oscars_nominees_by_category_FILMS_ENHANCED` containing CSV files for each award category:

- `Best_Picture.csv`
- `Actor_in_a_Leading_Role.csv`
- `Actress_in_a_Leading_Role.csv`
- `Writing_Original_Screenplay.csv`
- `Music_Original_Song.csv`
- And many more...

Each CSV file contains the following columns:
- `ceremony_year`: Year of the Oscar ceremony
- `category`: Award category name
- `film`: Film title
- `is_winner`: Boolean indicating if the film won (True) or was nominated (False)
- `source_url`: URL of the source page

## Dependencies

- `requests`: HTTP library for making web requests
- `beautifulsoup4`: HTML parsing library
- `python-dotenv`: Environment variable management
- Standard Python libraries: `argparse`, `csv`, `re`, `sys`, `time`, `pathlib`, `json`, `os`

## Notes

- The enhanced script is designed to be respectful to the Oscars website with built-in delays
- It handles various category name variations and normalizes them using historical category mapping
- Film titles are extracted using year-specific heuristics (different logic for early years 1929-1934)
- The script automatically deduplicates entries within each year/category/film combination
- Uses Bright Data's Browser API to bypass anti-scraping measures
- Credentials are stored securely in environment variables (not in code)
- Supports historical category evolution from 1929 to present
- Enhanced parsing logic prevents actor names from being treated as film titles
- Year-specific category detection for better accuracy in early Oscar years

## License

This project is for educational and research purposes. Please respect the Oscars website's terms of service when using this tool.
