import random

from fuzzywuzzy import fuzz

from components.fuzzy_matcher import fuzzy_match
from components.input_processor import process_input
from fuzzywuzzy import fuzz

from components.fuzzy_matcher import fuzzy_match
from components.input_processor import process_input


def calculate_confidence(processed_input, matched_patterns):
    # Create a list of tuples, where each tuple contains a pattern and its confidence score
    confidences = [(pattern, fuzz.partial_ratio(processed_input, pattern)) for pattern in matched_patterns]

    # Sort the list of tuples based on the confidence scores in descending order
    confidences.sort(key=lambda x: x[1], reverse=True)

    # Return the sorted list of tuples if it's not empty, otherwise return an empty list
    return confidences if confidences else []


def generate_response(intents, user_input_str):
    processed_input = process_input(user_input_str).lower()
    all_exact_matches = []
    all_fuzzy_matches = []

    # Iterate through each intent
    for intent in intents:
        # Process the intent patterns and convert them to lowercase
        processed_patterns = [process_input(pattern).lower() for pattern in intent['patterns']]

        # Search for exact matches with the same length
        exact_matches = [pattern for pattern in processed_patterns if
                         len(pattern) == len(processed_input) and pattern == processed_input]

        if exact_matches:
            all_exact_matches.append((exact_matches, intent['responses']))

        # Search for fuzzy matches
        fuzzy_threshold = 65
        fuzzy_matches = fuzzy_match(processed_input, processed_patterns, fuzzy_threshold)

        if fuzzy_matches:
            confidences = calculate_confidence(processed_input, fuzzy_matches)
            all_fuzzy_matches.append((confidences, intent['responses']))

    # Sort the exact matches by the highest confidence score
    all_exact_matches = sorted(all_exact_matches, key=lambda x: len(x[0][0]), reverse=True)

    # Sort the fuzzy matches by the highest confidence score
    all_fuzzy_matches = sorted(all_fuzzy_matches, key=lambda x: x[0][0][1], reverse=True)

    # Extract the best exact matches and responses
    best_exact_matches, best_exact_responses = all_exact_matches[0] if all_exact_matches else ([], [])

    # Extract the best fuzzy matches and responses
    best_fuzzy_matches, best_fuzzy_responses = all_fuzzy_matches[0] if all_fuzzy_matches else ([], [])

    # Print all exact and fuzzy matches for debugging purposes
    # print("Exact Matches:", all_exact_matches)
    # print("Fuzzy Matches:", all_fuzzy_matches)

    # Return the first response based on priority (exact match first, then fuzzy match)
    if best_exact_matches and best_exact_responses:
        return random.choice(tuple(best_exact_responses))
    elif best_fuzzy_matches and best_fuzzy_responses:
        return random.choice(tuple(best_fuzzy_responses))
    else:
        return "Sorry, I couldn't find a suitable response."

    return None
