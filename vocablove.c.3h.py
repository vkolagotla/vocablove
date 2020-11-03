#!/usr/bin/env python3

import re
import requests


def getWordsList():
    """Return list of words from the link."""

    # read raw html from the webpage
    r = requests.get("https://www.bestrandoms.com/random-german-words")
    text = r.text

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


# get 2 word list
# 6 new words for each list
word_list_1 = getWordsList()
word_list_2 = getWordsList()
words_12_list = word_list_1 + word_list_2

# create dictionary from list
word_itr = iter(words_12_list)
word_dict = dict(zip(word_itr, word_itr))

# print the words
for key, value in word_dict.items():
    if key != value:
        print(key + ": " + value)
