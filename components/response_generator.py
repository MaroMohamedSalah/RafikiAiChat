import random

from fuzzywuzzy import fuzz

from components.fuzzy_matcher import fuzzy_match
from components.input_processor import process_input


# from components.input_processor import process_input, tokenize_user_input
#
#
# def calculate_confidence(processed_input, matched_patterns):
#     confidences = [(pattern, fuzzy_partial_ratio(processed_input, pattern)) for pattern in matched_patterns]
#     confidences.sort(key=lambda x: x[1], reverse=True)  # Sort by confidence score in descending order
#     return confidences[0]  # Return the pattern with the highest confidence
#
# def generate_response(intent, user_input_str):
#     """
#     Generates a response based on the provided intent and user input.
#
#     Args:
#     - intent (dict): The intent object containing patterns and responses.
#     - user_input_str (str): The user's input string.
#
#     Returns:
#     - response (str): The generated response based on matching patterns.
#     """
#     processed_input = process_input(user_input_str).lower()
#
#     # Debugging exact match check
#     print("Processed Input:", processed_input)
#     processed_patterns = list(map(lambda pattern: process_input(pattern).lower(), intent['patterns']))
#     print("Processed Patterns:", processed_patterns)
#
#     processed_patterns = list(map(lambda pattern: process_input(pattern).lower(), intent['patterns']))
#
#     # Exact match check with the same length
#     exact_matches = [pattern for pattern in processed_patterns if
#                      len(processed_input) == len(pattern) and processed_input == pattern]
#     if exact_matches:
#         return random.choice(intent['responses'])
#
#     # Check if input length is less than 3 characters or contains less than 2 tokens, then return no response
#     # if len(processed_input) < 3 or len(tokenize_user_input(user_input_str)) < 2:
#     #     return None
#     #
#     # # Fuzzy match check with a higher threshold for input length >= 3
#     # fuzzy_threshold_high = 90
#     # fuzzy_high_matches = fuzzy_match(processed_input, intent['patterns'], fuzzy_threshold_high)
#     # if fuzzy_high_matches and all(len(processed_input) == len(pattern) for pattern in fuzzy_high_matches):
#     #     return random.choice(intent['responses'])
#     #
#     # # Fuzzy match check with a lower threshold for input length >= 3
#     # fuzzy_threshold_low = 65
#     # fuzzy_low_matches = fuzzy_match(processed_input, intent['patterns'], fuzzy_threshold_low)
#     # if fuzzy_low_matches and all(len(processed_input) == len(pattern) for pattern in fuzzy_low_matches):
#     #     return random.choice(intent['responses'])
#     #
#     # # If no direct or fuzzy match is found, check if any pattern is present in the processed input
#     # if any(pattern.lower() in processed_input for pattern in intent['patterns']):
#     #     return intent.get("response", "I don't understand.")
#
#     return None

def calculate_confidence(processed_input, matched_patterns):
    confidences = [(pattern, fuzz.partial_ratio(processed_input, pattern)) for pattern in matched_patterns]
    confidences.sort(key=lambda x: x[1], reverse=True)
    return confidences if confidences else []  # Return all matched patterns with their confidences



def generate_response(intents, user_input_str):
    processed_input = process_input(user_input_str).lower()
    all_fuzzy_matches = []

    for intent in intents:
        processed_patterns = list(map(lambda pattern: process_input(pattern).lower(), intent['patterns']))

        fuzzy_threshold = 80
        fuzzy_matches = fuzzy_match(processed_input, processed_patterns, fuzzy_threshold)

        if fuzzy_matches:
            confidences = calculate_confidence(processed_input, fuzzy_matches)
            all_fuzzy_matches.append((confidences, intent['responses']))

    all_fuzzy_matches = [(matches, responses) for matches, responses in all_fuzzy_matches if matches]
    all_fuzzy_matches = sorted(all_fuzzy_matches, key=lambda x: x[0][0][1], reverse=True)  # Sort by highest confidence

    print(all_fuzzy_matches)  # Print all matches with their scores

    best_fuzzy_matches, best_responses = all_fuzzy_matches[0] if all_fuzzy_matches else ([], [])

    if best_fuzzy_matches and best_responses:
        return best_responses[0]  # Returning the first response for the best fuzzy matches

    return None
