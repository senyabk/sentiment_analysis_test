import re

from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

import pickle

def text_preprocessor(txt):
    txt = re.sub(re.compile('<.*?>'), '', txt)
    txt = re.sub('[^A-Za-z0-9]+', ' ', txt)
    return txt.lower()


# Функция лемматизации
def text_lemmatizer(txt):
    lemmatizer = WordNetLemmatizer()
    tokens = word_tokenize(txt)
    return [lemmatizer.lemmatize(t) for t in tokens]

def make_prediction(text):
    vectorizer_filename = "./models/vectorizer.pkl"
    model_filename = "./models/model.pkl"

    with open(vectorizer_filename, 'rb') as file:
        pickle_vectorizer = pickle.load(file)

    with open(model_filename, 'rb') as file:
        pickle_model = pickle.load(file)

    x_pred = pickle_vectorizer.transform(text)
    return pickle_model.predict(x_pred)
