import re
import os
input_path = "songs"
global_dictionary = {}

def get_file_contents(path):
    with open(path) as f:
        content = f.read().lower()

    return content

def remove_symbols(filecontent):
    pattern = r"\-*\'*\b\w+"

    return re.findall(pattern, filecontent)

def count_words(array):
    word_dictionary = {}
    for word in array:
        if word != "":
            if word in word_dictionary:
                word_dictionary[word] += 1
            else:
                word_dictionary[word] = 1
    return word_dictionary


for filename in os.listdir(input_path):
    content = get_file_contents(os.path.join(input_path, filename))
    content = remove_symbols(content)
    dictionary = count_words(content)

    for name in dictionary.keys():
        if name not in global_dictionary.keys():
            global_dictionary[name] = 0

        global_dictionary[name] += dictionary[name]

for item in sorted(global_dictionary.items()):
    print(item)
