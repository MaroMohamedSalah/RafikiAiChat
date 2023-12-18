from components.input_processor import tokenize_user_input
from components.reinforcement_learning import choose_action, evaluate_response, update_q_value, print_q_table
from components.response_generator import generate_response
from components.user_name import extract_user_name


def chat(intents):
    states = set(' '.join(intent['patterns']) for intent in intents if 'patterns' in intent)
    Q = {state: [0] * len(intents) for state in states}
    feedback_dict = {}
    learning_rate = 0.3
    discount_factor = 0.7
    exploration_prob = 1

    print("Chatbot: Hi there! Type 'exit' to end the conversation.")

    while True:
        user_input_str = input("You: ")
        user_tokens = tokenize_user_input(user_input_str)
        user_input_str = ' '.join(user_tokens)

        if user_input_str.lower() == 'exit':
            print("Chatbot: Goodbye!")
            break

        response = generate_response(intents, user_input_str)  # Pass the 'intents' list
        user_name = extract_user_name(user_input_str)
        if user_name:
            print(f"rafikak: Hi {user_name}! How can I assist you today?")
            continue
        if response:
            print("Chatbot:", response)
            user_state = response

            if user_state not in Q:
                Q[user_state] = [0] * len(intents)

            action = choose_action(user_state, Q, exploration_prob)
            intent = intents[action]

            if 'responses' in intent and len(intent['responses']) > 0:
                reward = evaluate_response()

                # Accumulate user feedback in the dictionary
                if user_state not in feedback_dict:
                    feedback_dict[user_state] = 0
                feedback_dict[user_state] += reward
                print(feedback_dict)
                update_q_value(user_state, action, reward, Q, learning_rate, discount_factor)
                print(f"Selected Action: {action}, Q-Value: {Q[user_state][action]}")
                # print("Feedback Dict:", feedback_dict)
                # print_q_table(Q)

                # Learn from user feedback
                if reward == 1:
                    print("Chatbot: Thank you for your positive feedback! I'll try to remember that.")
                elif reward == -1:
                    print("Chatbot: I'm sorry to hear that. I'll try to improve.")

        # Print the word with the highest number in feedback_dict
    if feedback_dict:
        max_word = max(feedback_dict, key=feedback_dict.get)
        print(f"Chatbot: The Response with the highest feedback is: '{max_word}'")

    else:
        print("Chatbot: I'm sorry, I didn't understand that. Can you please rephrase?")
