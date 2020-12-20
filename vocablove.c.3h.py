#!/usr/bin/env python3

import os
import csv
import random
from typing import Dict


def get_words_local(word_file: str) -> Dict[str, str]:
    """Get words from a local word file.

    Parameters
    ----------
    word_file: str
        Path to the word file

    Returns
    -------
    Dict
        Returns a dictionary of words as string
    """
    with open(word_file, mode="r") as file:
        # reading the CSV file
        csv_file = csv.reader(file)
        local_words_dict = {}
        # displaying the contents of the CSV file
        for lines in csv_file:
            local_words_dict[lines[0]] = lines[1]

    return local_words_dict


def main():
    """Gets the file and prints the words to GNOME shell."""
    # get the python file path to use for words_list dir
    head, _ = os.path.split(os.path.abspath(__file__))

    # list of lang levels and respective word files
    word_file_list = [
        "word_sources/telc_a1_1.csv",
        "word_sources/telc_a1_2.csv",
        "word_sources/telc_a2_1.csv",
        "word_sources/telc_a2_2.csv",
        "word_sources/telc_b1_1.csv",
        "word_sources/telc_b1_2.csv",
        "word_sources/telc_b2_1.csv",
        "word_sources/telc_b2_2.csv",
    ]

    # get a random language level (A1 to C1)
    rand_lang_level = head + "/" + str(random.sample(word_file_list, 1)).strip("'[]'")

    # get 10 random words
    ten_randon_words = random.sample(get_words_local(rand_lang_level).items(), 10)
    # print the words to consol
    for key, value in ten_randon_words:
        if key != value:
            print(
                key.capitalize()
                + ": "
                + value.capitalize()
                + " | bash='word_to_speech {}' terminal=false".format(key)
            )
    print("---")
    # option to refresh the word list
    print("Refresh Words | refresh=true")
    # print respective lang level
    lang_level_dict = {
        "a1_1": "Level A1.1",
        "a1_2": "Level A1.2",
        "a2_1": "Level A2.1",
        "a2_2": "Level A2.2",
        "b1_1": "Level B1.1",
        "b1_2": "Level B1.2",
        "b2_1": "Level B2.1",
        "b2_2": "Level B2.2",
    }
    for key in lang_level_dict.keys():
        if key in rand_lang_level:
            print(lang_level_dict[key])
            print("---")
        else:
            pass


if __name__ == "__main__":
    main()
