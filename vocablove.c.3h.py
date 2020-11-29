#!/usr/bin/env python3

import re
import requests

german_words = "https://www.bestrandoms.com/random-german-words"


def getWordsList(word_source: str) -> list:
    """Returns a list of words from the link."""

    # read raw html from the webpage
    try:
        r = requests.get(word_source, timeout=7.0)
        text = r.text
    except requests.Timeout as e:
        print("Timeout Error")
        print(str(e))
    except requests.ConnectionError as e:
        print("Connection Error. Make sure you are connected to Internet.")
        print(str(e))

    # tag to get words from
    tag = "span"

    # filter the text based on class
    i = text.find('</div><div class="clearfix">')
    text = text[i:]
    i_2 = text.find('<div class="clearfix"></div></ul>')
    text = text[:i_2]

    # regex to extract required strings
    reg_str = "<" + tag + ">(.*?)</" + tag + ">"
    words_list = re.findall(reg_str, text)

    # capitalize the first word
    words_list = list(map(lambda s: s.capitalize(), words_list))

    return words_list


def getWordsDict():
    """Returns a dictionary of words with their translation."""
    # get 2 word list
    # 6 new words for each list
    word_list_1 = getWordsList(german_words)
    word_list_2 = getWordsList(german_words)
    words_12_list = word_list_1 + word_list_2

    # create dictionary from list
    word_itr = iter(words_12_list)
    word_dict = dict(zip(word_itr, word_itr))
    return word_dict


# print the words to consol
for key, value in getWordsDict().items():
    if key != value:
        print(key + ": " + value)

print("---")
# option to refresh the word list
print("Refresh Words | refresh=true")
