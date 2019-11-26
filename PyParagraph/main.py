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



dash_break = "-----------------------------"
print_lines = {
    "Paragraph Analysis \n" + dash_break + "\n"
    f"Approximate Word Count: {word_count} \n" + 
    f"Approximate Sentence Count: {sentence_count} \n" +
    f"Average Letter Count: {letter_count} \n" +
    f"Average Sentence Length: {sentence_length} \n" + dash_break
}

# Print & Export the Paragraph analysis text file:
analysis_file = open('Paragraph_analysis.txt','w+')
analysis_file.writelines(print_lines)
analysis_file.close()
analysis_file = open('Paragraph_analysis.txt','r+')
print(analysis_file.read())
