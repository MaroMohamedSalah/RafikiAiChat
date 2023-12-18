from fuzzywuzzy import fuzz


def fuzzy_partial_ratio(str1, str2):
    return fuzz.partial_ratio(str1, str2)


# def fuzzy_match(processed_input, processed_patterns, threshold):
#     high_matches = [pattern for pattern in processed_patterns if
#                     fuzzy_partial_ratio(processed_input, pattern) >= threshold]
#     return high_matches  # Returns patterns that match above the specified threshold
# def fuzzy_partial_ratio(str1, str2):
#     return fuzz.partial_ratio(str1, str2)


def fuzzy_match(processed_input, processed_patterns, threshold):
    high_matches = [
        pattern for pattern in processed_patterns
        if fuzzy_partial_ratio(processed_input, pattern) >= threshold
           and len(processed_input) - len(pattern) <= 5  # Check the difference in lengths
    ]
    return high_matches
def calculate_confidence(processed_input, matched_patterns):
    # Create a list of tuples, where each tuple contains a pattern and its confidence score
    confidences = [(pattern, fuzz.partial_ratio(processed_input, pattern)) for pattern in matched_patterns]

    # Sort the list of tuples based on the confidence scores in descending order
    confidences.sort(key=lambda x: x[1], reverse=True)

    # Return the sorted list of tuples if it's not empty, otherwise return an empty list
    return confidences if confidences else []