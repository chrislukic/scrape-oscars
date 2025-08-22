# Historical Oscar Categories Mapping
# This file contains the evolution of Oscar categories from 1929 to present

# Categories by era - when they were introduced and when they changed
CATEGORY_HISTORY = {
    # Early categories (1929-1930s)
    "1929": [
        "Outstanding Picture",
        "Best Actor",
        "Best Actress", 
        "Best Director",
        "Best Writing",
        "Best Cinematography",
        "Best Art Direction",
        "Best Engineering Effects"
    ],
    
    # 1930s additions
    "1930": [
        "Outstanding Picture",
        "Best Actor",
        "Best Actress",
        "Best Director", 
        "Best Writing",
        "Best Cinematography",
        "Best Art Direction",
        "Best Sound Recording"
    ],
    
    "1934": [
        "Outstanding Production",  # renamed from Outstanding Picture
        "Best Actor",
        "Best Actress",
        "Best Director",
        "Best Writing (Adaptation)",
        "Best Writing (Original Story)",
        "Best Cinematography",
        "Best Art Direction",
        "Best Sound Recording",
        "Best Assistant Director",
        "Best Film Editing",
        "Best Music (Scoring)",
        "Best Music (Song)"
    ],
    
    # 1940s additions
    "1940": [
        "Outstanding Production",
        "Best Actor",
        "Best Actress", 
        "Best Supporting Actor",  # added 1936
        "Best Supporting Actress",  # added 1936
        "Best Director",
        "Best Writing (Original Screenplay)",
        "Best Writing (Screenplay)",
        "Best Cinematography (Black and White)",
        "Best Cinematography (Color)",
        "Best Art Direction (Black and White)",
        "Best Art Direction (Color)",
        "Best Sound Recording",
        "Best Film Editing",
        "Best Music (Original Score)",
        "Best Music (Original Song)",
        "Best Special Effects",
        "Best Documentary (Short Subject)",
        "Best Documentary (Feature)"
    ],
    
    # 1950s-1960s
    "1950": [
        "Best Picture",  # renamed from Outstanding Production
        "Best Actor",
        "Best Actress",
        "Best Supporting Actor",
        "Best Supporting Actress", 
        "Best Director",
        "Best Writing (Story and Screenplay)",
        "Best Writing (Screenplay)",
        "Best Cinematography (Black and White)",
        "Best Cinematography (Color)",
        "Best Art Direction (Black and White)",
        "Best Art Direction (Color)",
        "Best Costume Design (Black and White)",
        "Best Costume Design (Color)",
        "Best Sound Recording",
        "Best Film Editing",
        "Best Music (Scoring of a Dramatic or Comedy Picture)",
        "Best Music (Scoring of a Musical Picture)",
        "Best Music (Original Song)",
        "Best Special Effects",
        "Best Documentary (Short Subject)",
        "Best Documentary (Feature)",
        "Best Foreign Language Film"
    ],
    
    # 1970s-1980s
    "1970": [
        "Best Picture",
        "Best Actor in a Leading Role",
        "Best Actress in a Leading Role",
        "Best Actor in a Supporting Role",
        "Best Actress in a Supporting Role",
        "Best Director",
        "Best Writing (Original Screenplay)",
        "Best Writing (Screenplay Based on Material from Another Medium)",
        "Best Cinematography",
        "Best Art Direction",
        "Best Costume Design",
        "Best Sound",
        "Best Film Editing",
        "Best Music (Original Dramatic Score)",
        "Best Music (Original Song Score)",
        "Best Music (Original Song)",
        "Best Visual Effects",
        "Best Documentary (Short Subject)",
        "Best Documentary (Feature)",
        "Best Foreign Language Film",
        "Best Short Film (Live Action)",
        "Best Short Film (Animated)"
    ],
    
    # 1990s-2000s
    "1990": [
        "Best Picture",
        "Best Actor in a Leading Role",
        "Best Actress in a Leading Role",
        "Best Actor in a Supporting Role",
        "Best Actress in a Supporting Role",
        "Best Director",
        "Best Writing (Original Screenplay)",
        "Best Writing (Screenplay Based on Material Previously Produced or Published)",
        "Best Cinematography",
        "Best Art Direction",
        "Best Costume Design",
        "Best Sound",
        "Best Sound Effects Editing",
        "Best Film Editing",
        "Best Music (Original Score)",
        "Best Music (Original Song)",
        "Best Makeup",
        "Best Visual Effects",
        "Best Documentary (Short Subject)",
        "Best Documentary (Feature)",
        "Best Foreign Language Film",
        "Best Short Film (Live Action)",
        "Best Short Film (Animated)"
    ],
    
    # 2000s-2010s
    "2000": [
        "Best Picture",
        "Best Actor in a Leading Role",
        "Best Actress in a Leading Role",
        "Best Actor in a Supporting Role",
        "Best Actress in a Supporting Role",
        "Best Director",
        "Best Writing (Original Screenplay)",
        "Best Writing (Adapted Screenplay)",
        "Best Cinematography",
        "Best Art Direction",
        "Best Costume Design",
        "Best Sound Mixing",
        "Best Sound Editing",
        "Best Film Editing",
        "Best Music (Original Score)",
        "Best Music (Original Song)",
        "Best Makeup",
        "Best Visual Effects",
        "Best Documentary (Short Subject)",
        "Best Documentary (Feature)",
        "Best Foreign Language Film",
        "Best Short Film (Live Action)",
        "Best Short Film (Animated)",
        "Best Animated Feature Film"
    ],
    
    # 2010s-2020s
    "2010": [
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
        "Best Sound Mixing",
        "Best Sound Editing",
        "Best Film Editing",
        "Best Music (Original Score)",
        "Best Music (Original Song)",
        "Best Makeup and Hairstyling",
        "Best Visual Effects",
        "Best Documentary (Short Subject)",
        "Best Documentary (Feature)",
        "Best International Feature Film",
        "Best Short Film (Live Action)",
        "Best Short Film (Animated)",
        "Best Animated Feature Film"
    ],
    
    # Current era (2020s)
    "2020": [
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
        "Best Sound",
        "Best Film Editing",
        "Best Music (Original Score)",
        "Best Music (Original Song)",
        "Best Makeup and Hairstyling",
        "Best Visual Effects",
        "Best Documentary (Short Subject)",
        "Best Documentary (Feature)",
        "Best International Feature Film",
        "Best Short Film (Live Action)",
        "Best Short Film (Animated)",
        "Best Animated Feature Film"
    ]
}

# Comprehensive mapping of all category variations
COMPREHENSIVE_CATEGORIES = {
    # Picture categories
    "Outstanding Picture": "Best Picture",
    "Outstanding Production": "Best Picture",
    "Best Picture": "Best Picture",
    
    # Acting categories
    "Best Actor": "Best Actor in a Leading Role",
    "Best Actor in a Leading Role": "Best Actor in a Leading Role",
    "Best Actress": "Best Actress in a Leading Role", 
    "Best Actress in a Leading Role": "Best Actress in a Leading Role",
    "Best Supporting Actor": "Best Actor in a Supporting Role",
    "Best Actor in a Supporting Role": "Best Actor in a Supporting Role",
    "Best Supporting Actress": "Best Actress in a Supporting Role",
    "Best Actress in a Supporting Role": "Best Actress in a Supporting Role",
    
    # Directing
    "Best Director": "Best Director",
    "Directing": "Best Director",
    
    # Writing categories
    "Best Writing": "Best Writing (Original Screenplay)",
    "Best Writing (Original Story)": "Best Writing (Original Screenplay)",
    "Best Writing (Adaptation)": "Best Writing (Adapted Screenplay)",
    "Best Writing (Story and Screenplay)": "Best Writing (Original Screenplay)",
    "Best Writing (Screenplay)": "Best Writing (Adapted Screenplay)",
    "Best Writing (Screenplay Based on Material from Another Medium)": "Best Writing (Adapted Screenplay)",
    "Best Writing (Screenplay Based on Material Previously Produced or Published)": "Best Writing (Adapted Screenplay)",
    "Best Writing (Original Screenplay)": "Best Writing (Original Screenplay)",
    "Best Writing (Adapted Screenplay)": "Best Writing (Adapted Screenplay)",
    
    # Technical categories
    "Best Cinematography": "Best Cinematography",
    "Best Cinematography (Black and White)": "Best Cinematography",
    "Best Cinematography (Color)": "Best Cinematography",
    
    "Best Art Direction": "Best Production Design",
    "Best Art Direction (Black and White)": "Best Production Design",
    "Best Art Direction (Color)": "Best Production Design",
    "Best Production Design": "Best Production Design",
    
    "Best Costume Design": "Best Costume Design",
    "Best Costume Design (Black and White)": "Best Costume Design",
    "Best Costume Design (Color)": "Best Costume Design",
    
    "Best Sound Recording": "Best Sound",
    "Best Sound": "Best Sound",
    "Best Sound Mixing": "Best Sound",
    "Best Sound Editing": "Best Sound",
    
    "Best Film Editing": "Best Film Editing",
    
    # Music categories
    "Best Music (Scoring)": "Best Music (Original Score)",
    "Best Music (Original Score)": "Best Music (Original Score)",
    "Best Music (Scoring of a Dramatic or Comedy Picture)": "Best Music (Original Score)",
    "Best Music (Original Dramatic Score)": "Best Music (Original Score)",
    "Best Music (Original Song Score)": "Best Music (Original Score)",
    "Best Music (Scoring of a Musical Picture)": "Best Music (Original Score)",
    
    "Best Music (Original Song)": "Best Music (Original Song)",
    "Best Music (Song)": "Best Music (Original Song)",
    
    # Effects categories
    "Best Engineering Effects": "Best Visual Effects",
    "Best Special Effects": "Best Visual Effects",
    "Best Visual Effects": "Best Visual Effects",
    
    "Best Makeup": "Best Makeup and Hairstyling",
    "Best Makeup and Hairstyling": "Best Makeup and Hairstyling",
    
    # Documentary categories
    "Best Documentary (Short Subject)": "Best Documentary (Short Subject)",
    "Best Documentary (Feature)": "Best Documentary (Feature)",
    
    # Short film categories
    "Best Short Film (Live Action)": "Best Short Film (Live Action)",
    "Best Short Film (Animated)": "Best Short Film (Animated)",
    
    # International/Foreign categories
    "Best Foreign Language Film": "Best International Feature Film",
    "Best International Feature Film": "Best International Feature Film",
    
    # Animated categories
    "Best Animated Feature Film": "Best Animated Feature Film",
    
    # Assistant Director (discontinued)
    "Best Assistant Director": "Best Assistant Director"
}

def get_categories_for_year(year):
    """Get the categories that were available in a given year."""
    # Find the closest year in our history
    available_years = sorted([int(y) for y in CATEGORY_HISTORY.keys()])
    
    # Find the year that's closest but not after the target year
    closest_year = None
    for y in available_years:
        if y <= year:
            closest_year = y
        else:
            break
    
    if closest_year is None:
        # If year is before 1929, return 1929 categories
        closest_year = 1929
    
    return CATEGORY_HISTORY[str(closest_year)]

def normalize_category(category_name, year=None):
    """Normalize a category name to its modern equivalent."""
    return COMPREHENSIVE_CATEGORIES.get(category_name, category_name)

def get_all_known_categories():
    """Get all known category names from the comprehensive mapping."""
    return set(COMPREHENSIVE_CATEGORIES.keys())

def get_modern_categories():
    """Get the modern (current) category names."""
    return set(COMPREHENSIVE_CATEGORIES.values())



