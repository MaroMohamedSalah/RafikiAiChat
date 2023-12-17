from nltk import RegexpTokenizer, pos_tag
from nltk.corpus import stopwords

from components.Chat_Bot import detect_language


def process_input(input_text):
    """
    Processes the input text by converting it to lowercase.

    Args:
    - input_text (str): The input text to be processed.

    Returns:
    - processed_input (str): Processed input text in lowercase.
    """
    processed_input = input_text.lower()
    return processed_input


def tokenize_user_input(user_input_str):
    """
    Tokenizes the user input string.

    Args:
    - user_input_str (str): The user input string to be tokenized.

    Returns:
    - tokens (list): List of tokens generated from the user input string.
    """
    lang = 'english'
    if detect_language(user_input_str) == 'ar':
        lang = "arabic"

    tokenizer = RegexpTokenizer(r'\w+')
    tokens = tokenizer.tokenize(user_input_str.lower())

    pos_tags = pos_tag(tokens)

    # stop_words = set(stopwords.words(lang))
    # tokens = [token for token in tokens if token not in stop_words]

    return tokens
