import re
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

def text_preprocessor(text):
    text = re.sub(re.compile('<.*?>'), '', text)
    text =  re.sub('[^A-Za-z0-9]+', ' ', text)
    return text.lower()


# Функция лемматизации
def text_lemmatizer(text):
    lemmatizer = WordNetLemmatizer()
    tokens = word_tokenize(text)
    return [lemmatizer.lemmatize(t) for t in tokens]