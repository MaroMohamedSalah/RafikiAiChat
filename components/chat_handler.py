from components.input_processor import tokenize_user_input
from components.response_generator import generate_response
from components.user_name import extract_user_name


def chat(intents):
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
            print("rafikak:", response)
        else:
            print("Chatbot: I'm sorry, I didn't understand that. Can you please rephrase?")
