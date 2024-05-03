
# Question 1
# Task 3: Programming and Research
    # 3.2: Using the ‘Auto Tokenizer’ function in the ‘Transformers’ library,
    # write a ‘function’ to count unique tokens in the text (.txt) and give the ‘Top 30’ words.

from transformers import AutoTokenizer
from collections import Counter
import csv

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
