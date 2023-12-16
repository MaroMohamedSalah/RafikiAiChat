from input_processor import tokenize_user_input
from intent_loader import load_intents_from_json
from response_generator import generate_response
from user_name import extract_user_name


def chatbot(intents):
    print("Chatbot: Hi there! Type 'exit' to end the conversation.")

    while True:
        user_input_str = input("You: ")
        user_tokens = tokenize_user_input(user_input_str)
        user_input_str = ' '.join(user_tokens)

        if user_input_str.lower() == 'exit':
            print("Chatbot: Goodbye!")
            break
            
        user_name = extract_user_name(user_input_str)
        if user_name:
            print(f"rafikak: Hi {user_name}! How can I assist you today?")
            continue
            
        response = None
        for intent in intents:
            response = generate_response(intent, user_input_str)

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
