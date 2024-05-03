
###############################################################################################
                                #HIT137 SOFTWARE NOW – Assignment 2#

# Lecturer name: Abhijith Beeravolu
# Group members: 
#        - Son Lam Nguyen (Justin) (Student ID: s377342)
#        - Chirag Dudhat (Student ID: s374835) 
# GitHub group link: https://github.com/son-lam-nguyen-s377342/HIT137_SOFTWARENOW_Assignment2.git

###############################################################################################
import os
import csv
import pandas as pd
from collections import Counter

# Question 1
# Task 1: Extract the ‘text’ in all the CSV files and store them into a single ‘.txt file’

# List of CSV file paths
csv_file_paths = [
    r'C:\Users\lamng\Downloads\HIT137-Software-Now\Assignment2\CSV\CSV1.csv', 
    r'C:\Users\lamng\Downloads\HIT137-Software-Now\Assignment2\CSV\CSV2.csv',
    r'C:\Users\lamng\Downloads\HIT137-Software-Now\Assignment2\CSV\CSV3.csv',
    r'C:\Users\lamng\Downloads\HIT137-Software-Now\Assignment2\CSV\CSV4.csv'
]
# Read and concatenate text from all CSV files
def extract_text_from_csv_files(csv_file_paths): 
    
    all_texts = []

    for file_path in csv_file_paths:
        if os.path.isfile(file_path):
            with open(file_path, 'r', encoding='utf-8') as file:
                reader = csv.reader(file)
                headers = next(reader)
                max_text_column = max(range(len(headers)), key=lambda i: sum(len(row[i]) for row in reader))
                file.seek(0)
                next(reader)  
                all_texts.extend(row[max_text_column].strip() for row in reader if len(row) > max_text_column)
        else:
            print(f"File '{file_path}' not found. Skipping.")

# Writing all extracted text to a new file
    output_text_file_path = r'C:\Users\lamng\Downloads\HIT137-Software-Now\Assignment2\combined_text.txt'
    with open(output_text_file_path, 'w', encoding='utf-8') as file:
        file.write('\n'.join(all_texts))
    print(f'Data extracted from all CSV files to {output_text_file_path}')

# Call the function to extract and write text
extract_text_from_csv_files(csv_file_paths)


# Task 3: Programming and Research
    # 3.1: Using any in-built library present in Python, count the occurrences of the words in the text (.txt)
    # and give the ‘Top 30’ most common words. And store the ‘Top 30’ common words and their counts into a CSV file.

txt_file_path = r'C:\Users\lamng\Downloads\HIT137-Software-Now\Assignment2\combined_text.txt'

with open(txt_file_path, 'r', encoding='utf-8') as file:
    words = file.read().split()
word_counts = Counter(words)
top_30_common_words = word_counts.most_common(30)

csv_file_path = r'C:\Users\lamng\Downloads\HIT137-Software-Now\Assignment2\top_30_common_words.csv'

with open(csv_file_path, 'w', newline='', encoding='utf-8') as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerow(['Word', 'Count'])
    csv_writer.writerows(top_30_common_words)

print(f'Top 30 common words saved to {csv_file_path}')

