from fuzzywuzzy import fuzz


def fuzzy_partial_ratio(str1, str2):
    return fuzz.partial_ratio(str1, str2)


def fuzzy_match(processed_input, processed_patterns, threshold):
    high_matches = [
        pattern for pattern in processed_patterns
        if fuzzy_partial_ratio(processed_input, pattern) >= threshold
           and len(processed_input) - len(pattern) <= 5  # Check the difference in lengths
    ]
    return high_matches  # Returns patterns that match above the specified threshold and meet the length difference condition
