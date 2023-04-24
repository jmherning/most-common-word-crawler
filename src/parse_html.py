import requests
import re
import string
from bs4 import BeautifulSoup
from nltk.tokenize import word_tokenize
import nltk
import numpy as np
import pandas as pd


DEFAULT_URL = "https://en.wikipedia.org/wiki/Microsoft"
DECIMAL_NUM_REGEX = r"^[+-]{0,1}((\d*\.)|\d*)\d+$"
HYPHENATED_NUM_REGEX = r"^\d+-\d+$"


def get_page_content(url: str = DEFAULT_URL):
    """Get the page conent of the input url."""

    return requests.get(DEFAULT_URL).content


def get_section_text(text: str):
    soup = BeautifulSoup(text, "html.parser")
    target = soup.find(id="History")

    section = []

    for sib in target.parent.find_next_siblings():
        if sib.name == "h2":
            break

        if sib.name == "p":
            section.append(sib.text)

    return section


def filter_words(text: str, exclude: list):
    try:
        tokens = word_tokenize(text)
    except LookupError:
        nltk.download("punkt")
        tokens = word_tokenize(text)

    punctuations = list(string.punctuation)

    tokens = [word for word in tokens if word not in punctuations]
    tokens = [word for word in tokens if not word.isdigit()]
    tokens = [word for word in tokens if re.match(DECIMAL_NUM_REGEX, word) is None]
    tokens = [word for word in tokens if re.match(HYPHENATED_NUM_REGEX, word) is None]
    tokens = [word for word in tokens if word not in exclude]

    return tokens


def count_words(words: []):
    series = pd.value_counts(np.array(words))
    df = series.to_frame()
    df = df.rename(columns={"count": "# of occurrences"})

    return df


def get_page_word_count(page: bytes, num: int, exclude: list):
    section_text = get_section_text(page)

    words = []
    for sentence in section_text:
        words += filter_words(sentence, exclude)

    word_count = count_words(words)

    return word_count.iloc[:num]
