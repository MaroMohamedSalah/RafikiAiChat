import random

from components.fuzzy_matcher import fuzzy_match,calculate_confidence,fuzzy_partial_ratio
from components.input_processor import process_input, tokenize_user_input


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
#     processed_patterns = list(map(lambda pattern: process_input(pattern).lower(), intent['patterns']))
#
#     # Exact match check with the same length
#     exact_matches = [pattern for pattern in processed_patterns if
#                      len(processed_input) == len(pattern) and processed_input == pattern]
#     if exact_matches:
#         return random.choice(intent['responses'])
#
#     # Check if input length is less than 3 characters or contains less than 2 tokens, then return no response
#     if len(processed_input) < 3 or len(tokenize_user_input(user_input_str)) < 2:
#         return None
#
#     # Fuzzy match check with a higher threshold for input length >= 3
#     fuzzy_threshold_high = 90
#     fuzzy_high_matches = fuzzy_match(processed_input, intent['patterns'], fuzzy_threshold_high)
#     if fuzzy_high_matches:
#         return random.choice(intent['responses'])
#
#     # Fuzzy match check with a lower threshold for input length >= 3
#     fuzzy_threshold_low = 65
#     fuzzy_low_matches = fuzzy_match(processed_input, intent['patterns'], fuzzy_threshold_low)
#     if fuzzy_low_matches:
#         return random.choice(intent['responses'])
#
#     # If no direct or fuzzy match is found, check if any pattern is present in the processed input
#     if any(pattern.lower() in processed_input for pattern in intent['patterns']):
#         return intent.get("response", "I don't understand.")
#
#     return None
# def calculate_confidence(processed_input, fuzzy_matches):
#     pass


def generate_response(intents, user_input_str):
    processed_input = process_input(user_input_str).lower()
    all_exact_matches = []
    all_fuzzy_matches = []

    # Iterate through each intent
    for intent in intents:
        # Check if 'patterns' key exists in the intent
        if 'patterns' in intent and isinstance(intent['patterns'], list):
            # Process the intent patterns and convert them to lowercase
            processed_patterns = [process_input(pattern).lower() for pattern in intent['patterns']]

            # Search for exact matches with the same length
            exact_matches = [pattern for pattern in processed_patterns if len(pattern) == len(processed_input) and pattern == processed_input]

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