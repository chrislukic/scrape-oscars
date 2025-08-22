#!/usr/bin/env python3
"""
Test script to validate enhanced parsing logic and compare with original parsing.
"""

import sys
import os
from pathlib import Path

# Add the current directory to Python path to import modules
sys.path.insert(0, str(Path(__file__).parent))

from enhanced_parsing import (
    enhanced_looks_like_category_heading,
    is_likely_actor_name,
    is_likely_film_title,
    is_early_years_format
)

def test_enhanced_parsing():
    """Test the enhanced parsing logic."""
    print("Testing Enhanced Oscar Parsing Logic")
    print("=" * 50)
    
    # Test early years format detection
    print("\n1. Testing Early Years Format Detection:")
    for year in [1928, 1929, 1930, 1934, 1935, 1940]:
        is_early = is_early_years_format(year)
        print(f"  {year}: {'Early Years' if is_early else 'Modern Years'}")
    
    # Test actor name detection
    print("\n2. Testing Actor Name Detection:")
    actor_tests = [
        "Mary Pickford",
        "Warner Baxter", 
        "George Arliss",
        "Norma Shearer",
        "Fredric March",
        "Helen Hayes",
        "Wallace Beery",
        "Charles Laughton",
        "Katharine Hepburn",
        "Leslie Howard",
        "Paul Muni",
        "Marie Dressler",
        "Lionel Barrymore",
        "Adolphe Menjou",
        "Ann Harding",
        "Irene Dunne",
        "Jackie Cooper",
        "Marlene Dietrich",
        "Richard Dix",
        "George Bancroft",
        "Bessie Love",
        "Betty Compson",
        "Chester Morris",
        "Corinne Griffith",
        "Jeanne Eagels",
        "Lewis Stone",
        "Ruth Chatterton"
    ]
    
    for actor in actor_tests:
        is_actor = is_likely_actor_name(actor)
        print(f"  '{actor}': {'Actor' if is_actor else 'Not Actor'}")
    
    # Test film title detection
    print("\n3. Testing Film Title Detection:")
    film_tests = [
        "Sunrise",
        "Wings", 
        "The Jazz Singer",
        "The Circus",
        "7th Heaven",
        "The Crowd",
        "The Racket",
        "Chang",
        "The Broadway Melody",
        "The Bridge of San Luis Rey",
        "The Patriot",
        "White Shadows in the South Seas",
        "All Quiet on the Western Front",
        "Cimarron",
        "Grand Hotel"
    ]
    
    for film in film_tests:
        is_film = is_likely_film_title(film)
        print(f"  '{film}': {'Film' if is_film else 'Not Film'}")
    
    # Test category heading detection for early years
    print("\n4. Testing Category Heading Detection (Early Years - 1929):")
    early_category_tests = [
        "Outstanding Picture",
        "Best Actor", 
        "Best Actress",
        "Best Director",
        "Best Writing",
        "Best Writing (Adaptation)",
        "Best Writing (Original Story)",
        "Best Writing (Title Writing)",
        "Best Cinematography",
        "Best Art Direction",
        "Best Engineering Effects",
        "Best Assistant Director",
        "Best Actor in a Leading Role",  # This shouldn't be detected in early years
        "Best Actress in a Leading Role",  # This shouldn't be detected in early years
        "Mary Pickford",  # Should not be detected as category
        "Sunrise",  # Should not be detected as category
        "Wings",  # Should not be detected as category
    ]
    
    for category in early_category_tests:
        is_category = enhanced_looks_like_category_heading(category, 1929)
        print(f"  '{category}': {'Category' if is_category else 'Not Category'}")
    
    # Test category heading detection for modern years
    print("\n5. Testing Category Heading Detection (Modern Years - 1950):")
    modern_category_tests = [
        "Best Picture",
        "Best Actor in a Leading Role",
        "Best Actress in a Leading Role", 
        "Best Actor in a Supporting Role",
        "Best Actress in a Supporting Role",
        "Best Director",
        "Best Writing (Original Screenplay)",
        "Best Writing (Adapted Screenplay)",
        "Best Cinematography",
        "Best Production Design",
        "Best Costume Design",
        "Best Film Editing",
        "Best Sound",
        "Best Music (Original Score)",
        "Best Music (Original Song)",
        "Best Visual Effects",
        "Best Makeup and Hairstyling",
        "Best Animated Feature Film",
        "Best Documentary (Feature)",
        "Best Documentary (Short Subject)",
        "Best Short Film (Live Action)",
        "Best Short Film (Animated)",
        "Best International Feature Film",
        "Mary Pickford",  # Should not be detected as category
        "Sunrise",  # Should not be detected as category
        "Wings",  # Should not be detected as category
    ]
    
    for category in modern_category_tests:
        is_category = enhanced_looks_like_category_heading(category, 1950)
        print(f"  '{category}': {'Category' if is_category else 'Not Category'}")
    
    print("\n" + "=" * 50)
    print("Enhanced parsing logic test completed!")

if __name__ == "__main__":
    test_enhanced_parsing()

