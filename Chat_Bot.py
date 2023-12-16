from nltk.corpus import stopwords
from contractions import fix
from nltk.tokenize import word_tokenize
import json
import re
import random
from langdetect import detect
def detect_language(text):
    try:
        language = detect(text)
        return language
    except Exception as e:
        # Handle exceptions such as short text or unsupported languages
        # print(f"Error detecting language: {e}")
        return 'unknown langauge please try again'

def user_input_tokinize(user_input):
    lang = 'english'
    if detect_language(user_input)=='ar':
        lang="arabic"
    # Handle contractions
    user_input = fix(user_input)
    # Tokenization Input
    tokens = word_tokenize(user_input.lower())
    # Remove stopwords
    stop_words = set(stopwords.words(lang))
    tokens = [token for token in tokens if token not in stop_words]
    # Remove punctuation
    # tokens = [token for token in tokens if token.isalpha()]
    return tokens
#


def load_intents_from_json(file_path):
    with open(file_path, 'r', encoding='utf-8') as json_file:
        intents = json.load(json_file)
    return intents['intents']



def rule_based_chatbot(user_input, intents):
    for intent in intents:
        for pattern in intent['patterns']:
            # matching
            if re.search(fr'\b{re.escape(pattern)}\b', user_input, flags=re.IGNORECASE):
                return random.choice(intent['responses'])

    # If no pattern is matched
    return ["I'm sorry, I don't understand that."]

# Example usage
def chat_with_bot():
    key=True
    while key:
        file_path = 'data_sets/college_info.json'
        intents = load_intents_from_json(file_path)
        user_input = input('user: ')
        if user_input.lower() in ['exit','bye']:
            print("Rafiki: I'm Happy for helping You")
            # key=False
            exit()
        else:
            user_input = user_input_tokinize(user_input)
            user_input = ' '.join(user_input)
            response = rule_based_chatbot(user_input, intents)
            print("Rafikak: ", response)


# chat_with_bot()

# def rule_based_response(entities, pos_tags):
#     # Rule-based logic for responding to user queries
#     for intent in intents_data['intents']:
#         if 'tag' in intent:
#             # Check if the entity or POS tag matches the intent's tag
#             if intent['tag'] in entities or intent['tag'] in [tag[0] for tag in pos_tags]:
#                 return intent['responses'][0]
#
#     # No matching rule found, provide a default response
#     return "I'm sorry, I don't understand your question."
#
# # Example usage
# user_input = "Where is lab 1?"
# entities, pos_tags = process_input(user_input)
# response = rule_based_response(entities, pos_tags)
# print(response)
# file_path = 'data_sets/rafiki-info-dataset.json'
# intents = load_intents_from_json(file_path)
# compiled_patterns = [re.compile(fr'\b{re.escape(pattern)}\b', flags=re.IGNORECASE) for intent in intents for pattern in intent['patterns']]
#
# def rule_based_chatbot(user_input, intents):
#     for compiled_pattern, intent in zip(compiled_patterns, intents):
#         if compiled_pattern.search(user_input):
#             return random.choice(intent['responses'])
#
#     return ["I'm sorry, I don't understand that."]