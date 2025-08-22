#!/usr/bin/env python3
"""
Test script to verify historical Oscar category mapping
"""

from oscar_categories_historical import (
    get_categories_for_year,
    normalize_category,
    get_all_known_categories,
    get_modern_categories
)

def test_category_mapping():
    """Test the category mapping functionality."""
    print("Testing Oscar Category Historical Mapping")
    print("=" * 50)
    
    # Test different years
    test_years = [1929, 1934, 1940, 1950, 1970, 1990, 2000, 2010, 2020]
    
    for year in test_years:
        print(f"\nYear {year}:")
        categories = get_categories_for_year(year)
        print(f"  Categories available: {len(categories)}")
        for cat in categories[:5]:  # Show first 5
            print(f"    - {cat}")
        if len(categories) > 5:
            print(f"    ... and {len(categories) - 5} more")
    
    # Test category normalization
    print(f"\n" + "=" * 50)
    print("Testing Category Normalization:")
    
    test_categories = [
        "Outstanding Picture",
        "Best Actor", 
        "Best Writing (Adaptation)",
        "Best Cinematography (Black and White)",
        "Best Art Direction",
        "Best Sound Recording",
        "Best Music (Scoring)",
        "Best Special Effects"
    ]
    
    for cat in test_categories:
        normalized = normalize_category(cat)
        print(f"  '{cat}' -> '{normalized}'")
    
    # Show statistics
    print(f"\n" + "=" * 50)
    print("Statistics:")
    all_categories = get_all_known_categories()
    modern_categories = get_modern_categories()
    
    print(f"Total known category variations: {len(all_categories)}")
    print(f"Modern category names: {len(modern_categories)}")
    print(f"\nModern categories:")
    for cat in sorted(modern_categories):
        print(f"  - {cat}")

if __name__ == "__main__":
    test_category_mapping()

