import json
import random

from nltk import pos_tag, word_tokenize
from nltk.corpus import stopwords
from contractions import fix
from Chat_Bot import detect_language

def load_intents_from_json(file_path):
    with open(file_path, 'r',encoding='utf-8') as file:
        data = json.load(file)
    return data['intents']

def tokenize_user_input(user_input_str):
    lang = 'english'
    if detect_language(user_input_str) == 'ar':
        lang = "arabic"

    # Handle contractions
    fixed_input = fix(user_input_str)

    # If fix returns a tuple, extract the fixed string
    if isinstance(fixed_input, tuple):
        fixed_input = fixed_input[0]

    # Tokenization Input
    tokens = word_tokenize(fixed_input.lower())
    pos_tags = pos_tag(tokens)

    # Remove stopwords
    stop_words = set(stopwords.words(lang))
    tokens = [token for token in tokens if token not in stop_words]

    return tokens

def get_response(intent, user_input_str):
    for pattern in intent['patterns']:
        if pattern.lower() in user_input_str.lower():
            return random.choice(intent['responses'])
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
json_file_path = 'data_sets/combine.json'  # Update this with your JSON file path
intents = load_intents_from_json(json_file_path)
chatbot(intents)
