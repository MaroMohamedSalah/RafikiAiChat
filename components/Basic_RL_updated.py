# # import json
# # import random
# # # import numpy as
# # import numpy as np
# # from fuzzywuzzy import fuzz
# # import Levenshtein
# #
# # from nltk import pos_tag, word_tokenize, RegexpTokenizer
# # from nltk.corpus import stopwords
# # from contractions import fix
# # from Chat_Bot import detect_language
# #
# #
# # def handle_input(input_string):
# #     result = ""
# #     for char in input_string:
# #         if len(result) == 0 or char != result[-1]:
# #             result += char
# #     return result
# #
# # def load_intents_from_json(file_paths):
# #     all_intents = []
# #     for file_path in file_paths:
# #         with open(file_path, 'r', encoding='utf-8') as file:
# #             data = json.load(file)
# #         all_intents.extend(data.get('intents', []))
# #     return all_intents
# #
# # def process_input(input_text):
# #     processed_input = handle_input(input_text.lower())
# #     return processed_input
# #
# # def tokenize_user_input(user_input_str):
# #     lang = 'english'
# #     if detect_language(user_input_str) == 'ar':
# #         lang = "arabic"
# #
# #     tokenizer = RegexpTokenizer(r'\w+')
# #     tokens = tokenizer.tokenize(user_input_str.lower())
# #
# #     pos_tags = pos_tag(tokens)
# #
# #     # stop_words = set(stopwords.words(lang))
# #     # tokens = [token for token in tokens if token not in stop_words]
# #
# #     return tokens
# #
# # def get_response(intent, user_input_str):
# #     processed_input = process_input(user_input_str).lower()
# #
# #     # Debugging exact match check
# #     # print("Processed Input:", processed_input)
# #     processed_patterns = list(map(lambda pattern: process_input(pattern).lower(), intent['patterns']))
# #     # print("Processed Patterns:", processed_patterns)
# #     # if isinstance(intent['patterns'], str):
# #     #     processed_patterns = [process_input(intent['patterns']).lower()]
# #     # elif isinstance(intent['patterns'], list):
# #     #     processed_patterns = list(map(lambda pattern: process_input(pattern).lower(), intent['patterns']))
# #     if 'patterns' in intent:
# #         patterns = intent['patterns']
# #
# #         # Ensure patterns is a list
# #         if isinstance(patterns, str):
# #             processed_patterns = [process_input(patterns).lower()]
# #         elif isinstance(patterns, list):
# #             processed_patterns = [process_input(pattern).lower() for pattern in patterns]
# #         else:
# #             return None
# #     # Exact match check with the same length
# #     exact_matches = [pattern for pattern in processed_patterns if len(processed_input) == len(pattern) and processed_input == pattern]
# #     if exact_matches:
# #         return tuple(intent['responses'])
# #
# #     # Fuzzy match check with a higher threshold
# #     fuzzy_high_matches = [pattern for pattern in intent['patterns'] if fuzz.partial_ratio(processed_input, process_input(pattern).lower()) >= 90 and len(processed_input) == len(pattern)]
# #     if fuzzy_high_matches:
# #         return tuple(intent['responses'])
# #
# #     # Fuzzy match check with a lower threshold
# #     fuzzy_low_matches = [pattern for pattern in intent['patterns'] if fuzz.partial_ratio(processed_input, process_input(pattern).lower()) >= 65 and len(processed_input) == len(pattern)]
# #     if fuzzy_low_matches:
# #         return tuple(intent['responses'])
# #
# #     # If no direct or fuzzy match is found, check if any pattern is present in the processed input
# #     if any(pattern.lower() in processed_input for pattern in intent['patterns']):
# #         return intent.get("response", "I don't understand.")
# #
# #     return None
# #
# #
# #
# #
# # def choose_action(state, Q, exploration_prob):
# #     if state not in Q:
# #         return random.choice(list(range(len(Q))))  # Explore
# #
# #     if np.random.rand() < exploration_prob:
# #         return random.choice(list(range(len(Q))))  # Explore
# #     else:
# #         return np.argmax(Q[state])  # Exploit
# #
# #
# # # Helper function to evaluate the response and assign reward
# # def evaluate_response():
# #     # Simulate user feedback
# #     # Return a positive reward for a correct response, and a negative reward for an incorrect response
# #     return 1 if input("Was that response helpful? (yes/no): ").lower() == 'yes' else -1
# #
# #
# # # Helper function to update Q-values
# # def update_q_value(state, action, reward, Q, learning_rate, discount_factor):
# #     current_q_value = Q[state][action]
# #     max_future_q_value = np.max(Q[state])
# #     new_q_value = (1 - learning_rate) * current_q_value + learning_rate * (
# #                 reward + discount_factor * max_future_q_value)
# #     Q[state][action] = new_q_value
# #
# # def chatbot_with_q_learning(intents):
# #     # Extract unique states (tags) from intents
# #     states = set(tuple(intent['patterns']) for intent in intents if 'patterns' in intent)
# #
# #     # Q-table initialization
# #     Q = {state: [0] * len(intents) for state in states}
# #
# #     # Q-learning parameters
# #     learning_rate = 0.2
# #     discount_factor = 0.8
# #     exploration_prob = 0.4
# #
# #     print("Chatbot: Hi there! Type 'exit' to end the conversation.")
# #
# #     while True:
# #         user_input_str = input("You: ")
# #         user_tokens = tokenize_user_input(user_input_str)
# #         user_input_str = ' '.join(user_tokens)
# #
# #         if user_input_str.lower() == 'exit':
# #             print("Chatbot: Goodbye!")
# #             break
# #
# #         # Find the intent with the highest Q-value for the user input
# #         user_state = get_response(intents,user_input_str)
# #
# #         # Ensure the state is in the Q-table
# #         if user_state not in Q:
# #             Q[user_state] = [0] * len(intents)
# #
# #         action = choose_action(user_state, Q, exploration_prob)
# #         intent = intents[action]
# #
# #         # Check if the intent has non-empty response patterns
# #         if 'responses' in intent and len(intent['responses']) > 0:
# #             response = random.choice(intent['responses'])
# #             # Print the response
# #             print("rafikak:", response)
# #
# #             # User feedback (reward)
# #             reward = evaluate_response()
# #
# #             # Q-value update
# #             update_q_value(user_state, action, reward, Q, learning_rate, discount_factor)
# #         else:
# #             print("Chatbot: I'm sorry, I didn't understand that. Can you please rephrase?")
# #
# #
# # # Helper function to detect the state (intent tag) from user input
# #
# #
# # # Main program
# # json_file_paths = ['data_sets/college_info.json','data_sets/jocks-datasets.json',  'data_sets/general-dataset.json','data_sets/rafiki-info-dataset.json','data_sets/student-assistant-dataset.json']
# # intents = load_intents_from_json(json_file_paths)
# # chatbot_with_q_learning(intents)
# import json
# import random
# import numpy as np
# from fuzzywuzzy import fuzz
# from nltk import pos_tag, word_tokenize, RegexpTokenizer
# from contractions import fix
# from Chat_Bot import detect_language
#
# def handle_input(input_string):
#     result = ""
#     for char in input_string:
#         if len(result) == 0 or char != result[-1]:
#             result += char
#     return result
#
# def load_intents_from_json(file_paths):
#     all_intents = []
#     for file_path in file_paths:
#         with open(file_path, 'r', encoding='utf-8') as file:
#             data = json.load(file)
#         all_intents.extend(data.get('intents', []))
#     return all_intents
#
# def process_input(input_text):
#     processed_input = handle_input(input_text.lower())
#     return processed_input
#
# def tokenize_user_input(user_input_str):
#     lang = 'english'
#     if detect_language(user_input_str) == 'ar':
#         lang = "arabic"
#
#     tokenizer = RegexpTokenizer(r'\w+')
#     tokens = tokenizer.tokenize(user_input_str.lower())
#
#     pos_tags = pos_tag(tokens)
#
#     return tokens
#
# def get_response(intent, user_input_str):
#     processed_input = process_input(user_input_str).lower()
#
#     # Check if 'patterns' key exists in the intent
#     if 'patterns' in intent:
#         patterns = intent['patterns']
#
#         # Ensure patterns is a list
#         if isinstance(patterns, str):
#             processed_patterns = [process_input(patterns).lower()]
#         elif isinstance(patterns, list):
#             processed_patterns = [process_input(pattern).lower() for pattern in patterns]
#         else:
#             return None  # Handle unexpected type (e.g., None)
#
#         # Debugging exact match check
#         # print("Processed Input:", processed_input)
#         # print("Processed Patterns:", processed_patterns)
#
#         # Exact match check with the same length
#         exact_matches = [pattern for pattern in processed_patterns if len(processed_input) == len(pattern) and processed_input == pattern]
#         if exact_matches:
#             return tuple(intent['responses'])
#
#         # Fuzzy match check with a higher threshold
#         fuzzy_high_matches = [pattern for pattern in processed_patterns if fuzz.partial_ratio(processed_input, pattern) >= 90 and len(processed_input) == len(pattern)]
#         if fuzzy_high_matches:
#             return tuple(intent['responses'])
#
#         # Fuzzy match check with a lower threshold
#         fuzzy_low_matches = [pattern for pattern in processed_patterns if fuzz.partial_ratio(processed_input, pattern) >= 65 and len(processed_input) == len(pattern)]
#         if fuzzy_low_matches:
#             return tuple(intent['responses'])
#
#         # If no direct or fuzzy match is found, check if any pattern is present in the processed input
#         if any(pattern.lower() in processed_input for pattern in processed_patterns):
#             return intent.get("response", "I don't understand.")
#
#     return None
#
# def choose_action(state, Q, exploration_prob):
#     if state not in Q:
#         return random.choice(list(range(len(Q))))  # Explore
#
#     if np.random.rand() < exploration_prob:
#         return random.choice(list(range(len(Q))))  # Explore
#     else:
#         return np.argmax(Q[state])  # Exploit
#
# def evaluate_response():
#     # Simulate user feedback
#     # Return a positive reward for a correct response, and a negative reward for an incorrect response
#     return 1 if input("Was that response helpful? (yes/no): ").lower() == 'yes' else -1
#
# def update_q_value(state, action, reward, Q, learning_rate, discount_factor):
#     current_q_value = Q[state][action]
#     max_future_q_value = np.max(Q[state])
#     new_q_value = (1 - learning_rate) * current_q_value + learning_rate * (
#                 reward + discount_factor * max_future_q_value)
#     Q[state][action] = new_q_value
#
# def chatbot_with_q_learning(intents):
#     # Extract unique states (tags) from intents
#     states = set(tuple(intent['tag']) for intent in intents if 'tag' in intent)
#
#     # Q-table initialization
#     Q = {state: [0] * len(intents) for state in states}
#
#     # Q-learning parameters
#     learning_rate = 0.2
#     discount_factor = 0.8
#     exploration_prob = 0.4
#
#     print("Chatbot: Hi there! Type 'exit' to end the conversation.")
#
#     while True:
#         user_input_str = input("You: ")
#         user_tokens = tokenize_user_input(user_input_str)
#         user_input_str = ' '.join(user_tokens)
#
#         if user_input_str.lower() == 'exit':
#             print("Chatbot: Goodbye!")
#             break
#
#         # Find the intent with the highest Q-value for the user input
#         user_state = None
#         for intent in intents:
#             response = get_response(intent, user_input_str)
#             if response is not None:
#                 user_state = response
#                 break
#
#         # Ensure the state is in the Q-table
#         if user_state not in Q:
#             Q[user_state] = [0] * len(intents)
#
#         action = choose_action(user_state, Q, exploration_prob)
#         intent = intents[action]
#
#         # Check if the intent has non-empty response patterns
#         if 'responses' in intent and len(intent['responses']) > 0:
#             response = random.choice(intent['responses'])
#             # Print the response
#             print("Chatbot:", response)
#
#             # User feedback (reward)
#             reward = evaluate_response()
#
#             # Q-value update
#             update_q_value(user_state, action, reward, Q, learning_rate, discount_factor)
#         else:
#             print("Chatbot: I'm sorry, I didn't understand that. Can you please rephrase?")
#
# # Main program
# json_file_paths = ['data_sets/college_info.json', 'data_sets/jocks-datasets.json', 'data_sets/general-dataset.json', 'data_sets/rafiki-info-dataset.json', 'data_sets/student-assistant-dataset.json']
# intents = load_intents_from_json(json_file_paths)
# chatbot_with_q_learning(intents)
import json
import random
import numpy as np
from fuzzywuzzy import fuzz
from nltk import pos_tag, word_tokenize, RegexpTokenizer
from Chat_Bot import detect_language

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
    processed_input = handle_input(input_text.lower())
    return processed_input

def tokenize_user_input(user_input_str):
    lang = 'english'
    if detect_language(user_input_str) == 'ar':
        lang = "arabic"

    tokenizer = RegexpTokenizer(r'\w+')
    tokens = tokenizer.tokenize(user_input_str.lower())

    pos_tags = pos_tag(tokens)

    return tokens

def get_response(intent, user_input_str):
    processed_input = process_input(user_input_str).lower()

    processed_patterns = list(map(lambda pattern: process_input(pattern).lower(), intent['patterns']))

    # Exact match check with the same length
    exact_matches = [pattern for pattern in processed_patterns if len(processed_input) == len(pattern) and processed_input == pattern]
    if exact_matches:
        return random.choice(intent['responses'])

    # Fuzzy match check with a higher threshold
    fuzzy_high_matches = [pattern for pattern in intent['patterns'] if fuzz.partial_ratio(processed_input, process_input(pattern).lower()) >= 90 and len(processed_input) == len(pattern)]
    if fuzzy_high_matches:
        return random.choice(intent['responses'])

    # Fuzzy match check with a lower threshold
    fuzzy_low_matches = [pattern for pattern in intent['patterns'] if fuzz.partial_ratio(processed_input, process_input(pattern).lower()) >= 65 and len(processed_input) == len(pattern)]
    if fuzzy_low_matches:
        return random.choice(intent['responses'])

    # If no direct or fuzzy match is found, check if any pattern is present in the processed input
    if any(pattern.lower() in processed_input for pattern in intent['patterns']):
        return intent.get("response", "I don't understand.")

    return None

def choose_action(state, Q, exploration_prob):
    if state not in Q:
        return random.choice(list(range(len(Q))))  # Explore

    if np.random.rand() < exploration_prob:
        return random.choice(list(range(len(Q))))  # Explore
    else:
        return np.argmax(Q[state])  # Exploit

def evaluate_response():
    return 1 if input("Was that response helpful? (yes/no): ").lower() == 'yes' else -1

def update_q_value(state, action, reward, Q, learning_rate, discount_factor):
    current_q_value = Q[state][action]
    max_future_q_value = np.max(Q[state])
    new_q_value = (1 - learning_rate) * current_q_value + learning_rate * (
                reward + discount_factor * max_future_q_value)
    Q[state][action] = new_q_value
def print_q_table(Q):
    for state, values in Q.items():
        print(f"State: {state}")
        print("Q-Values:", values)
        print()
def chatbot_with_q_learning(intents):
    states = set(tuple(intent['patterns']) for intent in intents if 'patterns' in intent)
    Q = {state: [0] * len(intents) for state in states}
    learning_rate = 0.2
    discount_factor = 0.8
    exploration_prob = 0.4

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
            user_state = response

            if user_state not in Q:
                Q[user_state] = [0] * len(intents)

            action = choose_action(user_state, Q, exploration_prob)
            intent = intents[action]

            # Check if the intent has non-empty response patterns
            if 'responses' in intent and len(intent['responses']) > 0:
                reward = evaluate_response()

                update_q_value(user_state, action, reward, Q, learning_rate, discount_factor)
                # print_q_table(Q)
        else:
            print("Chatbot: I'm sorry, I didn't understand that. Can you please rephrase?")

# Main program
json_file_paths = ['data_sets/college_info.json', 'data_sets/jocks-datasets.json', 'data_sets/general-dataset.json', 'data_sets/rafiki-info-dataset.json', 'data_sets/student-assistant-dataset.json']
intents = load_intents_from_json(json_file_paths)
chatbot_with_q_learning(intents)
