import json


def load_intents_from_json(file_paths):
    """
    Loads intent data from JSON files.

    Args:
    - file_paths (list): List of file paths to JSON files containing intent data.

    Returns:
    - all_intents (list): Combined list of intent data extracted from the JSON files.
    """
    all_intents = []
    for file_path in file_paths:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
        all_intents.extend(data.get('intents', []))
    return all_intents
