# Python Homework - PyParagraph
# Submitted by : Sheetal Bongale
# Python 3.7.4
# This Python script will automate the analysis of any passage using a set of metrics

import os
import csv
import re

word_count = 0
sentence_count = 0
letter_count = 0
sentence_length = 0

# User input to choose the file_number (1 or 2):
file_num = input("Enter the paragraph number: 1 or 2 ?")

# Sets file and start parsing:
file_path = os.path.join('raw_data', 'paragraph_'  + str(file_num) + '.txt')

'''
To test the paragraph given in the READ.md:
file_path = os.path.join ('raw_data', 'readme_example.txt')
'''

with open (file_path, 'r') as txt_file:
    paragraph = txt_file.read()
    words = re.split(r' ',paragraph)
    sentences = re.split(r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s',paragraph)

    # Count the number of words:
    word_count = len(words)

    # Count the number of sentences:
    sentence_count = len(sentences)

    # Calculate the average word length:
    letters = 0
    for word in words:
        letters += len(word)

    letter_count = round(letters/word_count,1)

    # Calculate words per sentence:
    sentence_length = round(word_count/sentence_count,1)

# Output print format:
dash_break = "-----------------------------"
print_lines = (
    "Paragraph Analysis " + str(file_num) + '\n' + dash_break + "\n"
    f"Approximate Word Count: {word_count} \n" + 
    f"Approximate Sentence Count: {sentence_count} \n" +
    f"Average Letter Count: {letter_count} \n" +
    f"Average Sentence Length: {sentence_length} \n" + dash_break
)

# Print & Export the Paragraph analysis text file:
analysis_file = open('paragraph_analysis_' + str(file_num) + '.txt','w+')
analysis_file.writelines(print_lines)
analysis_file.close()
analysis_file = open('paragraph_analysis_' + str(file_num) + '.txt','r+')
print(analysis_file.read())