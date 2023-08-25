import re
import os

from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

import pickle
from main.preproc import text_preprocessor, text_lemmatizer
vectorizer_filename = os.getcwd() + "/models/vectorizer.pkl"
model_filename = os.getcwd() + "/models/model.pkl"

with open(vectorizer_filename, 'rb') as file:
    pickle_vectorizer = pickle.load(file)

with open(model_filename, 'rb') as file:
    pickle_model = pickle.load(file)


def make_prediction(text):
    x_pred = pickle_vectorizer.transform(text)
    return pickle_model.predict(x_pred)
