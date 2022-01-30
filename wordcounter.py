import re
import os
import sys

global_dictionary = {}


def get_file_contents(path):
    with open(path) as f:
        content = f.read().lower()

    return content


def extract_words(text):
    pattern = r"\-*\'*\b\w+"

    return re.findall(pattern, text)


try:
    filenames = os.listdir(sys.argv[1])
except (IndexError, FileNotFoundError):
    print("Please submit a valid directory path as first command line argument")
    sys.exit(1)

for filename in filenames:
    content = get_file_contents(os.path.join(sys.argv[1], filename))
    word_list = extract_words(content)

    for word in word_list:
        if word not in global_dictionary.keys():
            global_dictionary[word] = 0

        global_dictionary[word] += 1

for item in sorted(global_dictionary.items()):
    print(item)
