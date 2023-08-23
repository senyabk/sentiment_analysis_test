#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
import re

from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer


def text_preprocessor(txt):
    txt = re.sub(re.compile('<.*?>'), '', txt)
    txt = re.sub('[^A-Za-z0-9]+', ' ', txt)
    return txt.lower()


# Функция лемматизации
def text_lemmatizer(txt):
    lemmatizer = WordNetLemmatizer()
    tokens = word_tokenize(txt)
    return [lemmatizer.lemmatize(t) for t in tokens]

def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sentiment_analysis_test.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
