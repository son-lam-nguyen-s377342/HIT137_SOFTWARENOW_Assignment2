
###############################################################################################
                                #HIT137 SOFTWARE NOW – Assignment 2#

# Lecturer name: Abhijith Beeravolu
# Group members: 
#        - Son Lam Nguyen (Justin) (Student ID: s377342) 
#        - Chirag Dudhat (Student ID: S374835)
# GitHub group link: https://github.com/son-lam-nguyen-s377342/HIT137_SOFTWARENOW_Assignment2.git

###############################################################################################

import os
import csv
import pandas as pd
from collections import Counter
from transformers import AutoTokenizer
import spacy
import torch
from tqdm import tqdm

# QUESTION 1

# TASK 1: EXTRACT THE ‘TEXT’ IN ALL THE CSV FILES AND STORE THEM INTO A SINGLE ‘.TXT FILE’

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


# TASK 3: PROGRAMMING AND RESEARCH

# Task 3.1: Using any in-built library present in Python, count the occurrences of the words in the text (.txt)
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

# Task 3.2: Using the ‘Auto Tokenizer’ function in the ‘Transformers’ library,
# write a ‘function’ to count unique tokens in the text (.txt) and give the ‘Top 30’ words.

def count_unique_tokens(text_file, model_name="dmis-lab/biobert-v1.1"):
    
    # Using BioBERT Tokenizer
    tokenizer = AutoTokenizer.from_pretrained(model_name)

    # Initialize a Counter to keep track of unique tokens
    unique_tokens = Counter()

    # Read the entire content of the text file
    with open(text_file, 'r', encoding='utf-8') as file:
        text = file.read()

    # Tokenize the text using the Auto Tokenizer
    tokens = tokenizer.tokenize(text)

    # Update the Counter with the token occurrences
    unique_tokens.update(tokens)

    # Get the top 30 most common tokens
    top_30_tokens = unique_tokens.most_common(30)

    # Write the results to a CSV file
    output_file = r'C:\Users\lamng\Downloads\HIT137-Software-Now\Assignment2\top_30_tokens.csv'
    with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        # Write header
        writer.writerow(['Token', 'Count'])
        # Write the top 30 tokens and their counts
        writer.writerows(top_30_tokens)

    print(f"Top 30 tokens and counts saved to: {output_file}")

# Input file:
input_text_file = r'C:\Users\lamng\Downloads\HIT137-Software-Now\Assignment2\combined_text.txt'

# Call the function to count unique tokens and retrieve top 30 tokens from the input text file
count_unique_tokens(input_text_file)

# TASK 4: NAMED-ENTITY RECOGNITION (NER)

# Extract the ‘diseases’, and ‘drugs’ entities in the ‘.txt file’ separately using ‘en_core_sci_sm’/’en_ner_bc5cdr_md’
# and biobert. And compare the differences between the two models (Example: Total entities detected by both of them,
# what’s the difference, check for most common words, and check the difference.)

# Load the scispaCy model for biomedical NER
ner_model_bc5cdr = spacy.load('en_ner_bc5cdr_md')

# Increase the max_length limit
ner_model_bc5cdr.max_length = 1500000  # Set to a value appropriate for the text length

# Path to the input text file
input_text_file_path = r'C:\Users\lamng\Downloads\HIT137-Software-Now\Assignment2\combined_text.txt'

# Read the text from the cleaned text file
with open(input_text_file_path, 'r', encoding='utf-8') as text_file:
    biomedical_text = text_file.read()

# Split the text into chunks of 100,000 characters
chunk_size = 1500000
text_chunks = [biomedical_text[i:i + chunk_size] for i in range(0, len(biomedical_text), chunk_size)]

# Print the total number of chunks
total_chunks = len(text_chunks)
print(f'Total number of chunks: {total_chunks}')

# Initialize counters for diseases and drugs
diseases_counts = Counter()
drugs_counts = Counter()

# Process each chunk using the biomedical NER model
for chunk in tqdm(text_chunks, desc="Processing Chunks", unit="chunk"):
    doc_bc5cdr = ner_model_bc5cdr(chunk)

    # Extract tokens and their entity types from the biomedical NER model output
    tokens_entities_bc5cdr = [(token.text, token.ent_type_) for token in doc_bc5cdr]

    # Separate diseases and drugs
    diseases_bc5cdr = [token[0] for token in tokens_entities_bc5cdr if token[1] == 'DISEASE']
    drugs_bc5cdr = [token[0] for token in tokens_entities_bc5cdr if token[1] == 'CHEMICAL']

    # Update counters
    diseases_counts.update(diseases_bc5cdr)
    drugs_counts.update(drugs_bc5cdr)

# Order entries by count in descending order
ordered_diseases = [(word, count) for word, count in diseases_counts.most_common()]
ordered_drugs = [(word, count) for word, count in drugs_counts.most_common()]

# Save word counts to a CSV file
output_csv_file_path = r'C:\Users\lamng\Downloads\HIT137-Software-Now\Assignment2\SciSpaCy_count.csv'
with open(output_csv_file_path, 'w', newline='', encoding='utf-8') as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerow(['Entity Type', 'Word', 'Count'])

    # Write diseases entries to CSV
    for word, count in ordered_diseases:
        csv_writer.writerow(['Disease', word, count])

    # Write drugs entries to CSV
    for word, count in ordered_drugs:
        csv_writer.writerow(['Drug', word, count])

print(f'Ordered word counts saved to {output_csv_file_path}')

# QUESTION 2

# CHAPTER 1: The Gatekeeper

#Load picture 
import time
from PIL import Image

#Generate number based on time
current_time = int(time.time())
generated_number = (current_time % 100) + 50

#Add code to generate algorithm
if generated_number % 2 == 0:
    generated_number += 10

print("Number Generated Based on time = " + str(generated_number))

#Open image, store dimensions and load pixel map  
img = Image.open("C:/Users/lamng/Downloads/HIT137-Software-Now/Assignment2/chapter1.jpg")
width, height = img.size
pixels = img.load()

redkey = 0

#Iterate over all pixels in the image
for x in range(width):
    for y in range(height):
        #get rbg values of pixel, add generated number to pixels
        r,g,b = img.getpixel((x,y))
        pixels[x,y] = (r+generated_number, g+generated_number, b+generated_number)
        #get new rgb values, store r value
        r,g,b = img.getpixel((x,y))
        redkey += r

print(f"The sum of all red pixel values in the new image = " + str(redkey))

#Save new image
img.save("C:/Users/lamng/Downloads/HIT137-Software-Now/Assignment2/chapter1out.png")


# CHAPTER 2: The Chamber of Strings

# Part 1

def string_splitter(s):
    # Ensure string length is greater than 16
    if len(s) < 16:
        return "The length of the string must be at least 16."
    
    # Create empty strings to hold numbers and letters separately
    numbers = []
    letters = []

    # Separate the characters and numbers into separate strings
    for char in s:
        if char.isdigit():
            numbers.append(char)
        elif char.isalpha():
            letters.append(char)

    # Check if the number is even for each number in the inputted/given string
    # If it is even, change its value to ASCII via ord() function

    for i in range(len(numbers)):
        if int(numbers[i]) % 2 == 0:
            numbers[i] = str(ord(numbers[i]))

    # Check if the letters separated are uppercase
    # If uppercase, change the value to ASCII via ord() function

    for i in range(len(letters)):
        if letters[i].isupper():
            letters[i] = str(ord(letters[i]))

    # Combine and return the amended numbers and letters list
    return ''.join(numbers + letters)

# Assignment given input and relevant output expected

s = "56aAww1984sktr235270aYmn145ss785fsq31D0" 
    # s = input("Enter a string to decode: ")
print(string_splitter(s)) 
    # Output: "554195652503550748152575653148a65wwsktra89mnssfsq68"

# Part 2

# famous quote
# parameters
text =  "VZ FRYSVFU VZCNGVRAG NAQ N YVGGYR VAFRPHER V ZNXR ZVFGNXRF V NZ BHG BS PBAGEBY \n NAQ NG GVZRF UNEQ GB UNAQYR OHG VS LBH PNAG UNAQYR ZR NG ZL JBEFG GURA LBH FHER NF \nURYY QBAG QRFREIR ZR NG ZL ORFG ZNEVYLA ZBAEBR"
key = 13
decoded_text = ""

#Iterate through encrypted text
for char in text:
    #If not a space modify ascii value by key
    if (ord(char) != 32):
        oldchar = char
        newchar = ord(oldchar) - key
        #If character gets lowered below capital alphabet(<A), circle back to end(Z)
        if newchar < 65:
            newchar += 26
        #Append Decrypted Character
        decoded_text += chr(newchar)
    #If character is space include it in the decryption
    else:
        print(ord(char))
        decoded_text += char
print(decoded_text)

# QUESTION 3: FIXING THE ERROR-PRONE CODES.
# Below is the code that is encrypted using a number. Once you decrypt the below code,
# it reveals the original code with many errors. Please fix them and explain them using comments (#).

# Function to find decryption key
def key():
    total = 0
    for i in range(5):
        for j in range(3):
            if i + j == 5:
                total += i + j
            else:
                total -= i - j

    counter = 0
    while counter < 5:
        if total < 13:
            total += 1
        elif total > 13:
            total -= 1
        else:
            counter += 2
    return total

print(f"The decryption key is: {key()}")

# Decryption function to decrypt the ‘encrypted code’ to the original code
def decrypt(encrypted_text, key):
    decrypted_text = ""
    for char in encrypted_text:
        if char.isalpha():
            shifted = ord(char) - key # Decrypting by shifting back
            if char.islower():
                if shifted < ord("a"):
                    shifted += 26
            elif char.isupper():
                if shifted < ord("A"):
                    shifted += 26
            decrypted_text += chr(shifted)
        else:
            decrypted_text += char
    return decrypted_text

# Encrypted code provided 
encrypted_code = """
tybony inevnoyr
100
zl_qvpg = {'xrl1': 'inyhr1', 'xrl2': 'inyhr2', 'xr13': 'inyhr3'}
qrs cebprff_ahzoref():
tybony tybony_inevnoyr ybpny_inevnoyr = 5
ahzoref= [1, 2, 3, 4, 5]
juvyr ybpny_inevnoyr > >:
vs ybpny inevnoyr % 2 == 0: ahzoref.erzbir(ybpny_inevnoyr)
ybpny inevnoyr -= 1
erghea ahzoref
zl_frg (1, 2, 3, 4, 5, 5, 4, 3, 2, 1} erfhyg- cebprff_ahzoref(ahzoref-z1_frg)
qrs zbqvsl_qvpg():
ybpny inevnoyr
10
zl_qvpg['xr14'] = ybpny_inevnoyr
zbqvs1_qvpg(5)
qrs hcqngr_tybony():
tybony tybony_inevnoyr
tybony_inevnoyr += 10
sbe v va enatr(5):
cevag(v)
v +- 1
vs zl_frg vf abg Abar naq zl_qvpg['xr14'] == 10: cevag("Pbaqvgvba zrg!")
vs 5 abg va z1_qvpg:
cevag("5 abg sbhaq va gur qvpgvbanel!")
cevag(tybony_inevnoyr)
cevag(zl_qvpg)
cevag(zl_frg)
"""

# Use the key to decrypt the entire block of code
key_used_for_decryption = 13
decrypted_code = decrypt(encrypted_code, key_used_for_decryption)

# Print the decrypted code
print("Decrypted code is:")
print(decrypted_code)

# Correct the errors code
# Global variable initialisation
global_variable = 100

# Dictionary initialisation
my_dict = {"key1": "value1", "key2": "value2", "key3": "value3"}

def process_numbers():
    local_variable = 5
    numbers = [1, 2, 3, 4, 5]
    while local_variable > 0:
        if local_variable % 2 == 0:
            if local_variable in numbers:
                numbers.remove(local_variable)
        local_variable -= 1
    return numbers

def modify_dict():
    local_variable = 10
    my_dict["key4"] = local_variable


def update_global():
    global global_variable
    global_variable += 10

if __name__ == "__main__":
    # Print heading for the corrected decrypted code
    print("Corrected decrypted code:")

    # Set initialisation
    my_set = {1, 2, 3, 4, 5}

    # Processing numbers and updating the dictionary
    result = process_numbers()
    modify_dict()

    # Updating the global variable
    update_global()

    # Loop for demonstration
    for i in range(5):
        print(i)

    # Conditional checks
    if my_set is not None and my_dict.get("key4") == 10:
        print("Condition met!")

    if 5 not in my_dict:
        print("5 not found in the dictionary!")

    # Printing results
    print(global_variable)
    print(my_dict)
    print(my_set)