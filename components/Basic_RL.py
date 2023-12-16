import json
import random
import numpy as np
from fuzzywuzzy import fuzz

from nltk import pos_tag, word_tokenize
from nltk.corpus import stopwords
from contractions import fix
from Chat_Bot import detect_language


def load_intents_from_json(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data['intents']

def handle_input(input_string):
    result = ""
    for char in input_string:
        if len(result) == 0 or char != result[-1]:
            result += char
    return result
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
def process_input(input_text):
    processed_input = handle_input(input_text.lower().replace(" ", ""))
    return processed_input

def get_response(intents, user_input_str):
    processed_input = process_input(user_input_str).lower()

    for intent in intents:
        processed_patterns = list(map(lambda pattern: process_input(pattern).lower(), intent['patterns']))
        # print("Processed Patterns:", processed_patterns)

        # Exact match check
        if processed_input in processed_patterns:
            return tuple(intent.get('responses', ["I don't understand that."]))

        # Fuzzy match check with a higher threshold
        elif any(fuzz.partial_ratio(processed_input, pattern) >= 90 for pattern in processed_patterns):
            return tuple(intent.get('responses', ["I don't understand that."]))

        # Fuzzy match check with a lower threshold
        elif any(fuzz.partial_ratio(processed_input, pattern) >= 65 for pattern in processed_patterns):
            return tuple(intent.get('responses', ["I don't understand that."]))

    return tuple(["I don't understand that."])


def detect_state(user_input_str, intents):
    for intent in intents:
        if any(pattern.lower() in user_input_str for pattern in intent['patterns']):
            return intent['tag']
    return None


# Helper function to choose an action based on Q-values
def choose_action(state, Q, exploration_prob):
    if state not in Q:
        return random.choice(list(range(len(Q))))  # Explore

    if np.random.rand() < exploration_prob:
        return random.choice(list(range(len(Q))))  # Explore
    else:
        return np.argmax(Q[state])  # Exploit


# Helper function to evaluate the response and assign reward
def evaluate_response():
    # Simulate user feedback
    # Return a positive reward for a correct response, and a negative reward for an incorrect response
    return 1 if input("Was that response helpful? (yes/no): ").lower() == 'yes' else -1


# Helper function to update Q-values
def update_q_value(state, action, reward, Q, learning_rate, discount_factor):
    current_q_value = Q[state][action]
    max_future_q_value = np.max(Q[state])
    new_q_value = (1 - learning_rate) * current_q_value + learning_rate * (
                reward + discount_factor * max_future_q_value)
    Q[state][action] = new_q_value

def chatbot_with_q_learning(intents):
    # Extract unique states (tags) from intents
    states = set(tuple(intent['tag']) for intent in intents if 'tag' in intent)

    # Q-table initialization
    Q = {state: [0] * len(intents) for state in states}

    # Q-learning parameters
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

        # Find the intent with the highest Q-value for the user input
        user_state = get_response(intents,user_input_str)

        # Ensure the state is in the Q-table
        if user_state not in Q:
            Q[user_state] = [0] * len(intents)

        action = choose_action(user_state, Q, exploration_prob)
        intent = intents[action]

        # Check if the intent has non-empty response patterns
        if 'responses' in intent and len(intent['responses']) > 0:
            response = random.choice(intent['responses'])
            # Print the response
            print("rafikak:", response)

            # User feedback (reward)
            reward = evaluate_response()

            # Q-value update
            update_q_value(user_state, action, reward, Q, learning_rate, discount_factor)
        else:
            print("Chatbot: I'm sorry, I didn't understand that. Can you please rephrase?")


# Helper function to detect the state (intent tag) from user input


# Main program
json_file_path = '../data_sets/college_info.json'  # Update this with your JSON file path
intents = load_intents_from_json(json_file_path)
chatbot_with_q_learning(intents)
