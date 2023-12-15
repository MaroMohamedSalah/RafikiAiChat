import json
import random
import Levenshtein

from textblob import TextBlob
from nltk import pos_tag, word_tokenize
from nltk.corpus import stopwords
from contractions import fix
from Chat_Bot import detect_language
from fuzzywuzzy import fuzz
from nltk.stem import WordNetLemmatizer


def handle_input(input_string):
    result = ""
    for char in input_string:
        if len(result) == 0 or char != result[-1]:
            result += char
    return result


def load_intents_from_json(file_paths):
    all_intents = []
    for file_path in file_paths:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
        all_intents.extend(data.get('intents', []))
    return all_intents


def process_input(input_text):
    processed_input = handle_input(input_text.lower().replace(" ", ""))
    return processed_input


def tokenize_user_input(user_input_str):
    lang = 'english'
    if detect_language(user_input_str) == 'ar':
        lang = "arabic"

    # Skip spell correction for certain words (e.g., names)
    skip_correction_words = ['marawan', 'sa', 'mohamed']  # Add more names as needed
    if any(word.lower() in user_input_str.lower() for word in skip_correction_words):
        fixed_input = user_input_str
    else:
        fixed_input = fix(user_input_str)
        # Spell correction using TextBlob
        fixed_input = str(TextBlob(fixed_input.lower()).correct())

        if isinstance(fixed_input, tuple):
            fixed_input = fixed_input[0]

    tokens = word_tokenize(fixed_input.lower())
    pos_tags = pos_tag(tokens)

    stop_words = set(stopwords.words(lang))
    tokens = [token for token in tokens if token not in stop_words]

    return tokens


def get_response(intent, user_input_str):
    processed_input = process_input(user_input_str).lower()

    # Debugging exact match check
    print("Processed Input:", processed_input)
    processed_patterns = list(map(lambda pattern: process_input(pattern).lower(), intent['patterns']))
    print("Processed Patterns:", processed_patterns)

    # Exact match check
    if processed_input in processed_patterns:
        return random.choice(intent['responses'])

    # Fuzzy match check with a higher threshold
    elif any(fuzz.partial_ratio(processed_input, process_input(pattern).lower()) >= 90 for pattern in
             intent['patterns']):
        return random.choice(intent['responses'])

    # Fuzzy match check with a lower threshold
    elif any(fuzz.partial_ratio(processed_input, process_input(pattern).lower()) >= 80 for pattern in
             intent['patterns']):
        return random.choice(intent['responses'])

    # If no direct or fuzzy match is found, check if any pattern is present in the processed input
    if any(pattern.lower() in processed_input for pattern in intent['patterns']):
        return intent.get("response", "I don't understand that.")

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
json_file_paths = ['data_sets/jocks-datasets.json', 'data_sets/college_info.json', 'data_sets/general-dataset.json',
                   'data_sets/rafiki-info-dataset.json', 'data_sets/student-assistant-dataset.json']
intents = load_intents_from_json(json_file_paths)
chatbot(intents)

