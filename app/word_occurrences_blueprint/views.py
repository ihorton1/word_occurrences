import operator
import re
from collections import Counter

import requests
from bs4 import BeautifulSoup
from flask import Blueprint, request, render_template
from app.word_occurrences_blueprint.utils.regex import leading_punctuation, trailing_punctuation

word_occurrences = Blueprint('word_occurrences', __name__, template_folder='templates')

@word_occurrences.route('/health')
def health():
    return 'ok'

@word_occurrences.route('/', methods=['GET', 'POST'])
def word_count():
    errors = []
    results = {}
    if request.method == "POST":
        try:
            webpage_text = _get_url_response()
        except Exception as e:
            errors.append(e)
            return render_template('word_occurrences.html', errors=errors)

        # Create beautiful soup object and extract text
        text_string = _parse_html_text(webpage_text)
        text_list = text_string.split(sep=" ")

        # remove punctuation & numbers (but retain contractions and special characters)
        word_list = _remove_nonwords_from_list(text_list)

        # remove leading punctuation
        word_list = _trim_punctuation_from_strings(word_list, leading_punctuation)

        # remove trailing punctuation
        word_list = _trim_punctuation_from_strings(word_list, trailing_punctuation)

        word_count = Counter(word_list)

        # save the results
        results = _sort_words(word_count)

    return render_template('word_occurrences.html', errors=errors, results=results)


def _sort_words(word_count):
    results = sorted(
        word_count.items(),
        key=operator.itemgetter(0)  # Sorts in alphabetical order
    )
    return results


def _trim_punctuation_from_strings(word_list, regex):
    word_list = [re.sub(regex, repl='', string=w) for w in word_list]
    return word_list


def _remove_nonwords_from_list(text_list):
    only_words = re.compile('.*[A-Za-z].*')
    word_list = [w for w in text_list if only_words.match(w)]
    return word_list


def _parse_html_text(html):
    text_string = BeautifulSoup(html, 'html.parser').get_text(separator=" ")
    return text_string


def _get_url_response():
    url = request.form['url']
    response = requests.get(url)
    return response.text