#!/usr/bin/env python3

import re
import os
import csv
import random
import requests
from typing import List, Dict

german_words = "https://www.bestrandoms.com/random-german-words"


def getWordsList(word_source: str) -> List[str]:
    """Returns a list of words from the link.

    Parameters
    ----------
    word_source: str
        Website link to get the words

    Returns
    -------
    List
        Returns a list of words as strings
    """
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


def getWordsDict() -> Dict[str, str]:
    """Returns a dictionary of words with their translation.

    Returns
    -------
    Dict
        Returns a dictionary of words as strings
    """
    # get 2 word lists, max 6 new words for a list
    word_list_1 = getWordsList(german_words)
    word_list_2 = getWordsList(german_words)
    words_12_list = word_list_1 + word_list_2

    # create dictionary from list
    word_itr = iter(words_12_list)
    word_dict = dict(zip(word_itr, word_itr))
    return word_dict


def get_words_local(word_file: str) -> Dict[str, str]:
    """Get words from a local word file."""
    with open(word_file, mode="r") as file:
        # reading the CSV file
        csv_file = csv.reader(file)
        local_words_dict = {}
        # displaying the contents of the CSV file
        for lines in csv_file:
            local_words_dict[lines[0]] = lines[1]

    return local_words_dict


def main():
    # get the python file path to use for words_list dir
    head, _ = os.path.split(os.path.abspath(__file__))

    # list of lang levels and respective word files
    word_file_list = ["word_sources/telc_a1_1.csv", "word_sources/telc_a1_2.csv"]

    # get a random language level (A1 to C1)
    rand_lang_level = head + "/" + str(random.sample(word_file_list, 1)).strip("'[]'")

    # get 10 random words
    ten_randon_words = random.sample(get_words_local(rand_lang_level).items(), 10)
    # print the words to consol
    for key, value in ten_randon_words:
        if key != value:
            print(key.capitalize() + ": " + value.capitalize())
    print("---")
    # option to refresh the word list
    print("Refresh Words | refresh=true")
    # print respective lang level
    if "a1_1" in rand_lang_level:
        print("Level A1.1")
        print("---")
    else:
        print("Level A1.2")
        print("---")


if __name__ == "__main__":
    main()
