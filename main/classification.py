import os

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import LinearSVC
from sklearn.metrics import classification_report, confusion_matrix, ConfusionMatrixDisplay

import pickle


def make_prediction(text):
    vectorizer_filename = "C:/models/vectorizer.pkl"
    model_filename = "C:/models/model.pkl"

    with open(vectorizer_filename, 'rb') as file:
        pickle_vectorizer = pickle.load(file)

    with open(model_filename, 'rb') as file:
        pickle_model = pickle.load(file)

    x_pred = pickle_vectorizer.transform(text)
    return pickle_model.predict(x_pred)