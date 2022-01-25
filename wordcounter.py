import re
import os

input_path = "songs"
global_dictionary = {}


def get_file_contents(path):
    with open(path) as f:
        content = f.read().lower()

    return content


def filter_out_words(filecontent):
    pattern = r"\-*\'*\b\w+"

    return re.findall(pattern, filecontent)


for filename in os.listdir(input_path):
    content = get_file_contents(os.path.join(input_path, filename))
    word_list = filter_out_words(content)

    for word in word_list:
        if word not in global_dictionary.keys():
            global_dictionary[word] = 0

        global_dictionary[word] += 1

for item in sorted(global_dictionary.items()):
    print(item)
