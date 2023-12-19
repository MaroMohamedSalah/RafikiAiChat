from components.chat_handler import chat
from components.intent_loader import load_intents_from_json

json_file_paths = ['data_sets/college_info.json',
                   'data_sets/jocks-datasets.json',
                   # 'data_sets/general-dataset.json',
                   'data_sets/rafiki-info-dataset.json',
                   'data_sets/student-assistant-dataset.json']

intents = load_intents_from_json(json_file_paths)
chat(intents)
