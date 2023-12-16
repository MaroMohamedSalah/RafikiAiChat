import random

from fuzzy_matcher import fuzzy_match
from input_processor import process_input, tokenize_user_input
from intent_loader import load_intents_from_json


def get_response(intent, user_input_str):
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
    if fuzzy_high_matches:
        return random.choice(intent['responses'])

    # Fuzzy match check with a lower threshold for input length >= 3
    fuzzy_threshold_low = 65
    fuzzy_low_matches = fuzzy_match(processed_input, intent['patterns'], fuzzy_threshold_low)
    if fuzzy_low_matches:
        return random.choice(intent['responses'])

    # If no direct or fuzzy match is found, check if any pattern is present in the processed input
    if any(pattern.lower() in processed_input for pattern in intent['patterns']):
        return intent.get("response", "I don't understand.")

    return None


def chatbot(intents):
    print("Chatbot: Hi there! Type 'exit' to end the conversation.")

    while True:
        user_input_str = input("You: ")
        user_tokens = tokenize_user_input(user_input_str)
        user_input_str = ' '.join(user_tokens)

        if user_input_str.lower() == 'exit':
            print("Chatbot: Goodbye!")
            break

        response = None
        for intent in intents:
            response = get_response(intent, user_input_str)

            if response:
                break

        if response:
            print("rafikak:", response)
        else:
            print("Chatbot: I'm sorry, I didn't understand that. Can you please rephrase?")


# Main program
json_file_paths = ['data_sets/college_info.json', 'data_sets/jocks-datasets.json', 'data_sets/general-dataset.json',
                   'data_sets/rafiki-info-dataset.json', 'data_sets/student-assistant-dataset.json']
intents = load_intents_from_json(json_file_paths)
chatbot(intents)
