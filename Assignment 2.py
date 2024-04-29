
###############################################################################################
                                #HIT137 SOFTWARE NOW – Assignment 2#

# Lecturer name: Abhijith Beeravolu
# Group members: 
#        - Son Lam Nguyen (Student ID: s377342)
#        - Chirag Dudhat (Student ID: s374835) 
# GitHub group link: https://github.com/son-lam-nguyen-s377342/HIT137_SOFTWARENOW_Assignment2.git

###############################################################################################
import os
import csv
import re
import pandas as pd
from collections import Counter
from transformers import AutoTokenizer

# Question 1
# Task 1: Extract the ‘text’ in all the CSV files and store them into a single ‘.txt file’

# Paths to the CSV files
csv_file_paths = [
    'C:\Users\lamng\Downloads\HIT137-Software-Now\Assignment2\CSV\CSV1.csv', 
    'C:\Users\lamng\Downloads\HIT137-Software-Now\Assignment2\CSV\CSV2.csv',
    'C:\Users\lamng\Downloads\HIT137-Software-Now\Assignment2\CSV\CSV3.csv',
    'C:\Users\lamng\Downloads\HIT137-Software-Now\Assignment2\CSV\CSV4.csv'
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
output_txt_path = r'C:\Users\lamng\Downloads\HIT137-Software-Now\Assignment2\combined_text.txt'
with open(output_txt_path, 'w', encoding='utf-8') as file:
    file.write('\n'.join(all_texts))
print(f'Combined txt Built saved to {output_txt_path}')



    # Iterate over each file in the specified folder
    for file_name in os.listdir(zip_folder_path):
        if file_name.endswith('.csv'):
            file_path = os.path.join(zip_folder_path, file_name)

            # Read the CSV file using pandas
            df = pd.read_csv(file_path)

            # Assuming the column containing large text is named 'text', concatenate all text
            if 'text' in df.columns:
                text_column = df['text'].astype(str)  # Convert to string type
                concatenated_text += ' '.join(text_column) + '\n\n'  # Append to concatenated_text

    # Write the concatenated text to the output text file
    with open(output_txt_file, 'w', encoding='utf-8') as f:
        f.write(concatenated_text)

    print(f"Text extracted from CSV files and saved to: {output_txt_file}")


