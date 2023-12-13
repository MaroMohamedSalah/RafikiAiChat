# # # # # import nltk
# # # # # from nltk.tokenize import word_tokenize
# # # # # from nltk.tag import pos_tag
# # # # # from nltk.chunk import ne_chunk
# # # # # # nltk.download('all')
# # # # # # nltk.download('punkt')
# # # # # # nltk.download('maxent_ne_chunker')
# # # # # # nltk.download('words')
# # # # #
# # # # # def process_user_input(user_input):
# # # # #     # Tokenize the user's input into words
# # # # #     tokens = word_tokenize(user_input)
# # # # #
# # # # #     # Part-of-speech tagging
# # # # #     tagged_tokens = pos_tag(tokens)
# # # # #
# # # # #     # Named entity recognition
# # # # #     named_entities = ne_chunk(tagged_tokens)
# # # # #
# # # # #     # Extract intent and entities
# # # # #     intent = None
# # # # #     entities = {}
# # # # #
# # # # #     # Extract intent (currently, it's just the main verb)
# # # # #     for word, pos in tagged_tokens:
# # # # #         if pos.startswith('VB'):
# # # # #             intent = word
# # # # #             break
# # # # #
# # # # #     # Extract entities (currently, it's just proper nouns)
# # # # #     for subtree in named_entities:
# # # # #         if isinstance(subtree, nltk.Tree) and subtree.label() == 'GPE':
# # # # #             entities['location'] = ' '.join([token[0] for token in subtree])
# # # # #
# # # # #     return intent, entities
# # # # #
# # # # # # Example usage
# # # # # user_input = "Book a flight from New York to London tomorrow"
# # # # # intent, entities = process_user_input(user_input)
# # # # #
# # # # # print("Intent:", intent)
# # # # # print("Entities:", entities)
# # # # import nltk
# # # # from nltk.tokenize import word_tokenize
# # # #
# # # # # nltk.download('punkt')
# # # #
# # # #
# # # # def tokenize_patterns(patterns):
# # # #     tokenized_patterns = []
# # # #
# # # #     for pattern in patterns:
# # # #         tokens = word_tokenize(pattern)
# # # #         tokenized_patterns.append(tokens)
# # # #
# # # #     return tokenized_patterns
# # # #
# # # #
# # # # # Example usage
# # # # greeting_patterns = ["Hello", "Hi", "Hey there", "Good morning", "Greetings"]
# # # # tokenized_greeting_patterns = tokenize_patterns(greeting_patterns)
# # # #
# # # # print("Original Patterns:", greeting_patterns)
# # # # print("Tokenized Patterns:", tokenized_greeting_patterns)
# # # import nltk
# # # from nltk.tokenize import word_tokenize
# # # from nltk.tag import pos_tag
# # # from nltk.chunk import ne_chunk
# # # import numpy
# # #
# # #
# # # def process_user_input(user_in):
# # #     # Tokenize the user's input into words
# # #     tokens = word_tokenize(user_in)
# # #
# # #     # Part-of-speech tagging
# # #     tagged_tokens = pos_tag(tokens)
# # #
# # #     # Named entity recognition
# # #     named_entities = ne_chunk(tagged_tokens)
# # #
# # #     # Extract intent and entities
# # #     intent = None
# # #     entities = {}
# # #
# # #     # Extract intent (currently, it's just the main verb)
# # #     for word, pos in tagged_tokens:
# # #         if pos.startswith('VB'):
# # #             intent = word
# # #             break
# # #
# # #     # Extract entities (currently, it's just proper nouns)
# # #     for subtree in named_entities:
# # #         if isinstance(subtree, nltk.Tree) and subtree.label() == 'GPE':
# # #             entities['location'] = ' '.join([token[0] for token in subtree])
# # #
# # #     return intent, entities
# # #
# # # # Example usage
# # # user_in = "it specialization"
# # # intent, entities = process_user_input(user_in)
# # #
# # # print("Intent:", intent)
# # # print("Entities:", entities)
# # import nltk
# # from nltk.tokenize import word_tokenize
# # from nltk.tag import pos_tag
# # from nltk.chunk import ne_chunk
# # from nltk.corpus import stopwords
# #
# #
# #
# # def process_user_input(user_input):
# #     # Tokenize the user's input into words
# #     tokens = word_tokenize(user_input)
# #
# #     # Remove stop words
# #     stop_words = set(stopwords.words('english'))
# #     tokens = [word for word in tokens if word.lower() not in stop_words]
# #
# #     # Part-of-speech tagging
# #     tagged_tokens = pos_tag(tokens)
# #
# #     # Named entity recognition
# #     named_entities = ne_chunk(tagged_tokens)
# #
# #     # Extract intent and entities
# #     intent = None
# #     entities = {}
# #
# #     # Extract intent (currently, it's just the main verb)
# #     for word, pos in tagged_tokens:
# #         if pos.startswith('VB'):
# #             intent = word
# #             break
# #
# #     # Extract entities (currently, it's just proper nouns)
# #     for subtree in named_entities:
# #         if isinstance(subtree, nltk.Tree) and subtree.label() == 'GPE':
# #             entities['location'] = ' '.join([token[0] for token in subtree])
# #
# #     return intent, entities
# #
# # # Example usage
# # user_input_en = "hall 3?"
# # user_input_ar = "فين مكان الشؤون؟"
# #
# # intent_en, entities_en = process_user_input(user_input_en)
# # intent_ar, entities_ar = process_user_input(user_input_ar)
# #
# # print("English Input - Intent:", intent_en)
# # print("English Input - Entities:", entities_en)
# #
# # print("Arabic Input - Intent:", intent_ar)
# # print("Arabic Input - Entities:", entities_ar)
# import nltk
# from nltk.tokenize import word_tokenize
# from nltk.corpus import stopwords
# import spacy
#
# from nltk.stem import ISRIStemmer
# from nltk.stem import PorterStemmer
#
# # nltk.download('punkt')
# # nltk.download('stopwords')
#
# # def process_patterns(data):
# #     words = []
# #     docs_x = []
# #     docs_y = []
# #     labels = []
# #     tok=[]
# #
# #     for intent in data["intents"]:
# #         for pattern in intent["patterns"]:
# #             wrds = word_tokenize(pattern)
# #             words.extend(wrds)
# #             docs_x.append(wrds)
# #             docs_y.append(intent["tag"])
# #
# #         if intent["tag"] not in labels:
# #             labels.append(intent["tag"])
# #
# #     stop_words = set(stopwords.words("english"))
# #     words = [w.lower() for w in words if w.lower() not in stop_words]
# #
# #     ps = PorterStemmer()
# #     words = [ps.stem(w) for w in words]
# #
# #     # words = sorted(list(set(words)))
# #     tok.append(words)
# #     labels = sorted(labels)
# #
# #     return words, docs_x, docs_y, labels,tok
# #
# # # Example usage
# # data = {
# #     "intents": [
# #         {"tag":"room",
# #             "patterns":["room 1","room 2","where is room 1","where is room 2","where room 1","where room 2"],
# #             "responses": ["In Floor 0","In Basement"],
# #             "context_set":""
# #             },{"tag":"lab",
# #     "patterns":["lab 1","lab 2","lab 3","lab 4","lab 5","lab 6","where is lab 1","where is lab 2",
# #     "where is lab 3","where is lab 4","where is lab 5","where is lab 6","where lab 1","where lab 2",
# #     "where lab 3","where lab 4","where lab 5","where lab 6"],
# #     "responses": ["In Floor 1","in the right when You inter fcaih"],
# #     "context_set":""
# # }
# #
# #         # Add more intents as needed
# #     ]
# # }
# #
# # english_words, english_docs_x, english_docs_y, english_labels ,tok= process_patterns(data)
# # print("English Words:", english_words)
# # print("English Docs X:", english_docs_x)
# # print("English Docs Y:", english_docs_y)
# # print("English Labels:", english_labels)
# # print(tok)
# import nltk
# from nltk.corpus import stopwords
# from contractions import fix
# from nltk.tokenize import word_tokenize
# def user_input_tokinize(user_input):
#     # Handle contractions
#     user_input = fix(user_input)
#     # Tokenization Input
#     tokens = word_tokenize(user_input.lower())
#     # Remove stopwords
#     stop_words = set(stopwords.words("english"))
#     tokens = [token for token in tokens if token not in stop_words]
#     # Remove punctuation
#     tokens = [token for token in tokens if token.isalpha()]
#     return tokens
#
# us="is rafiki helps us ??"
# us2=user_input_tokinize(us)
# print(us2)
# sentence= ' '.join(us2)
# print(sentence)
# # from spellchecker.core import SpellChecker
# # from indexer import DictionaryIndex
# # def correct_spelling(sentence):
# #     # Tokenize the sentence
# #     tokens = word_tokenize(sentence)
# #
# #     # Initialize the spellchecker
# #     spell = SpellChecker()
# #
# #     # Identify misspelled words
# #     misspelled = spell.unknown(tokens)
# #
# #     # Correct misspelled words
# #     corrected_tokens = [spell.correction(word) if word in misspelled else word for word in tokens]
# #
# #     # Reconstruct the corrected sentence
# #     corrected_sentence = ' '.join(corrected_tokens)
# #
# #     return corrected_sentence
# # print(correct_spelling("plai fotball gren"))
# # print(fix(" I can't believe it's raining today."))
# # if sentence in ["class 4","where class 4","where is class 4"]:
# #     print("In Floor 4")
# # elif sentence in["doctor amr","doctor amr ghoniem","amr","amr ghoniem"]:
# #     print("he is ai doc")
# # else:
# #     print("f")
#
#
#
#
#
#
#
# # for pattern in intent["patterns"]:
# #     tokens = word_tokenize(pattern.lower())  # tokanize
# #     stop_words = set(stopwords.words("english"))  # remove stop words
# #     tokens = [token for token in tokens if token not in stop_words]
# #     words.extend(tokens)
# #     docs_x.append(tokens)
# #     docs_y.append(intent["tag"])
#
# # spacy.cli.download("en_core_web_sm")
# #
# # nlp = spacy.load("en_core_web_sm")
# #
# # # Process a text using the NLP pipeline
# # doc = nlp("This is an example sentence.")
# #
# # # Accessing various linguistic annotations
# # for token in doc:
# #     print(token.text, token.pos_, token.dep_)
# # import spacy
# #
# # # Load the English NLP model
# # nlp = spacy.load("en_core_web_sm")
# # doc = nlp("where is amr")
# # for token in doc:
# #     print(token.text, token.pos_, token.dep_)
#
# # # Define a simple rule-based chatbot
# # def rule_based_chatbot(user_input):
# #     # Process the user input using spaCy
# #     doc = nlp(user_input)
# #     # print(doc)
# #     # Initialize responses
# #     response = "I'm sorry, I didn't understand that."
# #
# #     # Check for a greeting
# #     # for token in doc:
# #     #     if token.text.lower() in ["ai specialization" ,"specialization ai","ai"]:
# #     #         response ="your nessessory subjects Convex optimization, AI , Machine Learning & Big Data then you can choose 2 subjects from rest"
# #     #         break
# #     for token in doc:
# #         if token.text.lower() in ["class-4","where class-4","where is class-4"]:
# #             response =["In Floor 4"]
# #             break
# #
# #     # Check for an information request
# #     if "information" in [token.text.lower() for token in doc] and "about" in [token.text.lower() for token in doc]:
# #         response = "Sure! I can provide information. What specific information are you looking for?"
# #
# #     return response ,doc
# #
# # # Example usage
# # user_input = input("User: ")
# # response = rule_based_chatbot(user_input)
# # print("Bot:", response)
#
# # data="who is doctor amr"
# # data = [sentence.lower() for sentence in data]
# #
# # # Join the list into a single string
# # data_as_string = ' '.join(data)
# #
# # x=nltk.sent_tokenize(data_as_string)
# # r="no"
# # for token in x:
# #     if token.text.lower() in ["ai specialization", "specialization ai", "ai"]:
# #         r="yes"
# #         break
# # user_input = input("User: ")
# # response =r
# # print("Bot:", response)
# # print(x)
# import nltk
# from nltk.tokenize import word_tokenize
# from nltk import pos_tag, ne_chunk, WordNetLemmatizer
#
# # Download necessary resources (punkt tokenizer and maxent_ne_chunker)
# # nltk.download('punkt')
# # nltk.download('maxent_ne_chunker')
# # nltk.download('words')
#
# # Example sentence
# # sentence = "John and Mary are going to the United States in May to discuss natural language processing."
# #
# # # Tokenization
# # tokens = word_tokenize(sentence)
# #
# # # Part-of-speech tagging
# # pos_tags = pos_tag(tokens)
# #
# # # Named Entity Recognition (NER)
# # ner_tags = ne_chunk(pos_tags)
#
# # Print results
# # print("Tokenization:")
# # print(tokens)
# #
# # print("\nPart-of-speech tagging:")
# # print(pos_tags)
# #
# # print("\nNamed Entity Recognition:")
# # print(ner_tags)
from nltk import pos_tag
from nltk.corpus import stopwords
from contractions import fix
from nltk.tokenize import word_tokenize
import json
import re
import random
from langdetect import detect

from Chat_Bot import detect_language



# def user_input_tokinize(user_input):
#     lang = 'english'
#     if detect_language(user_input) == 'ar':
#         lang = "arabic"
#
#     # Handle contractions
#     fixed_input = fix(user_input)
#
#     # If fix returns a tuple, extract the fixed string
#     if isinstance(fixed_input, tuple):
#         fixed_input = fixed_input[0]
#
#     # Tokenization Input
#     tokens = word_tokenize(fixed_input.lower())
#     pos_tags = pos_tag(tokens)
#
#     # Remove stopwords
#     stop_words = set(stopwords.words(lang))
#     tokens = [token for token in tokens if token not in stop_words]
#
#     return tokens, pos_tags
# def load_intents_from_json(file_path):
#     with open(file_path, 'r', encoding='utf-8') as json_file:
#         intents = json.load(json_file)
#     return intents['intents']
#
# def rule_based_response(user_input, intents_data):
#     # Tokenize the user input and get POS tags
#     tokens, pos_tags = user_input_tokinize(user_input)
#     # tokens=' '.join(tokens)
#
#     # Rule-based logic for responding to user queries
#     for intent in intents_data['intents']:
#         if 'tag' in intent:
#             # Check if the entity or POS tag matches the intent's tag
#             if intent['tag'] in tokens or intent['tag'] in [tag[0] for tag in pos_tags]:
#                 return intent['responses'][0]
#
#     # No matching rule found, provide a default response
#     return "I'm sorry, I don't understand your question."
# # def rule_based_response(user_input, intents_data):
# #     # Tokenize the user input and get POS tags
# #     tokens, pos_tags = user_input_tokinize(user_input)
# #     tokens = ' '.join(tokens)
# #     # Rule-based logic for responding to user queries
# #     for intent in intents_data:
# #         if 'tag' in intent and 'patterns' in intent:
# #             # Check if the entity or POS tag matches the intent's tag
# #             if any(tag in tokens or tag in [tag[0] for tag in pos_tags] for tag in intent['tag']):
# #                 return random.choice(intent['responses'])
#
#     # No matching rule found, provide a default response
#     # return "I'm sorry, I don't understand your question."
#
# # Example usage
# def chat_with_bot():
#     key = True
#     while key:
#         file_path = 'data_sets/rafiki-info-dataset.json'
#         intents = load_intents_from_json(file_path)
#         user_input = input('user: ')
#         if user_input.lower() in ['exit', 'bye']:
#             print("Rafiki: I'm Happy for helping You")
#             exit()
#         else:
#             response = rule_based_response(user_input,intents)
#             print("Rafikak: ", response)
#
#
# chat_with_bot()
# print(hi)
def detect_language(text):
    try:
        language = detect(text)
        return language
    except Exception as e:
        return 'unknown langauge please try again'
def user_input_tokinize(user_input):
    lang = 'english'
    if detect_language(user_input) == 'ar':
        lang = "arabic"

    # Handle contractions
    fixed_input = fix(user_input)

    # If fix returns a tuple, extract the fixed string
    if isinstance(fixed_input, tuple):
        fixed_input = fixed_input[0]

    # Tokenization Input
    tokens = word_tokenize(fixed_input.lower())
    pos_tags = pos_tag(tokens)

    # Remove stopwords
    stop_words = set(stopwords.words(lang))
    tokens = [token for token in tokens if token not in stop_words]

    return tokens, pos_tags


def rule_based_response(user_input, intents_data):
    # Tokenize the user input and get POS tags
    tokens, pos_tags = user_input_tokinize(user_input)
    # tokens=' '.join(tokens)
    # Rule-based logic for responding to user queries
    for intent in intents_data:
        if 'tag' in intent:
            # Check if the entity or POS tag matches the intent's tag
            if intent['tag'] in tokens or intent['tag'] in [tag[0] for tag in pos_tags]:
                return intent['responses'][0]

    # No matching rule found, provide a default response
    return "I'm sorry, I don't understand your question."

def load_intents_from_json(file_path):
    with open(file_path, 'r', encoding='utf-8') as json_file:
        intents = json.load(json_file)
    return intents['intents']

# Example usage
def chat_with_bot():
    key = True
    while key:
        file_path = 'data_sets/rafiki-info-dataset.json'
        intents = load_intents_from_json(file_path)
        user_input = input('user: ')
        if user_input.lower() in ['exit', 'bye']:
            print("Rafiki: I'm Happy for helping You")
            exit()
        else:
            response = rule_based_response(user_input, intents)
            print("Rafikak: ", response)

chat_with_bot()
