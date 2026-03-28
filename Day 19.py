# Write a function which count number of lines and number of words in a text. All the files are in the data the folder: a) Read obama_speech.txt file and count number of lines and words b) Read michelle_obama_speech.txt file and count number of lines and words c) Read donald_speech.txt file and count number of lines and words d) Read melina_trump_speech.txt file and count number of lines and words
import os

def count_lines_and_words(file_path):
    """
    Counts the number of lines and words in a given text file.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            line_count = len(lines)
            # Count words by splitting each line and summing the length of the lists
            word_count = sum(len(line.split()) for line in lines)
            return line_count, word_count
    except FileNotFoundError:
        return None, None

# List of filenames in the 'data' directory
data_folder = "data"
files = [
    "obama_speech.txt",
    "michelle_obama_speech.txt",
    "donald_speech.txt",
    "melina_trump_speech.txt"
]

# Iterate through each file and print results
for file_name in files:
    file_path = os.path.join(data_folder, file_name)
    lines, words = count_lines_and_words(file_path)
    
    if lines is not None:
        print(f"File: {file_name}")
        print(f"  Number of lines: {lines}")
        print(f"  Number of words: {words}\n")
    else:
        print(f"Error: {file_name} not found in '{data_folder}' directory.\n")
