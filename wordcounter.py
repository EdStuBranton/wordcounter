import re
import os
path_of_folder = "somewhere on your computer"
filepath = f'{path_of_folder}'
final_dictionary = {}

#----functions----#
""" The open_file function opens a file via a context manager and returns
    the content of the file as lowercase characters
"""
def open_file(filename):
    with open(f'{filepath}\{filename}') as f:
        content = f.read().lower()
    return content

"""
The unwanted_char_check function receives its data from the open_file function
and uses regex to split the content into a list while excluding symbols,
white space characters and other symbols that are not considered to be words.
"""
def unwanted_char_check(filecontent):
    pattern = r"\-*\'*\b\w+"
    clean_content = re.findall(pattern, filecontent)
    return clean_content

def words_counter(array):
    word_dictionary = {}
    for word in array:
        if word != "":
            if word in word_dictionary:
                word_dictionary[word] += 1
            else:
                word_dictionary[word] = 1
    return word_dictionary

#----actual processing----#

for filename in os.listdir(filepath):
    content_of_file = open_file(filename)
    cleaned_up_content = unwanted_char_check(content_of_file)
    result = words_counter(cleaned_up_content)

    for name in result.keys():
        if name in final_dictionary.keys():
            final_dictionary[name] += result[name]
        else:
            final_dictionary[name] = result[name]

print({k: v for k, v in sorted(final_dictionary.items(), key=lambda item: item[1])})
