import random

from components.fuzzy_matcher import fuzzy_match
from components.input_processor import process_input, tokenize_user_input


def generate_response(intent, user_input_str):
    """
    Generates a response based on the provided intent and user input.

    Args:
    - intent (dict): The intent object containing patterns and responses.
    - user_input_str (str): The user's input string.

    Returns:
    - response (str): The generated response based on matching patterns.
    """
    processed_input = process_input(user_input_str).lower()
    processed_patterns = list(map(lambda pattern: process_input(pattern).lower(), intent['patterns']))

    # Exact match check with the same length
    exact_matches = [pattern for pattern in processed_patterns if
                     len(processed_input) == len(pattern) and processed_input == pattern]
    if exact_matches:
        return random.choice(intent['responses'])

    # Check if input length is less than 3 characters or contains less than 2 tokens, then return no response
    if len(processed_input) < 3 or len(tokenize_user_input(user_input_str)) < 2:
        return None

    # Fuzzy match check with a higher threshold for input length >= 3
    fuzzy_threshold_high = 90
    fuzzy_high_matches = fuzzy_match(processed_input, intent['patterns'], fuzzy_threshold_high)
    if fuzzy_high_matches and all(len(processed_input) == len(pattern) for pattern in fuzzy_high_matches):
        return random.choice(intent['responses'])

    # Fuzzy match check with a lower threshold for input length >= 3
    fuzzy_threshold_low = 65
    fuzzy_low_matches = fuzzy_match(processed_input, intent['patterns'], fuzzy_threshold_low)
    if fuzzy_low_matches and all(len(processed_input) == len(pattern) for pattern in fuzzy_low_matches):
        return random.choice(intent['responses'])

    # If no direct or fuzzy match is found, check if any pattern is present in the processed input
    if any(pattern.lower() in processed_input for pattern in intent['patterns']):
        return intent.get("response", "I don't understand.")

    return None
