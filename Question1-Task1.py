
import os
import csv

# Question 1
# Task 1: Extract the ‘text’ in all the CSV files and store them into a single ‘.txt file’

# Paths to the CSV files
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
