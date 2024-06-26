# -*- coding: utf-8 -*-
"""Assignment.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1ICFIrHNSKRyQY8AWxaOjTsJNuhVnnMEk
"""

import pandas as pd
from transformers import AutoTokenizer, AutoModel

# Load the CSV file
csv_file_path = 'CSV2.csv'
data = pd.read_csv(csv_file_path)

# Check the columns in the CSV file to determine which column contains the text
data.head()

# Extracting the 'TEXT' column data
texts = data['TEXT']

# Path for the new text file to store extracted texts
output_txt_path = 'extracted_texts.txt'

# Writing texts into a single '.txt' file
with open(output_txt_path, 'w', encoding='utf-8') as file:
    for text in texts:
        file.write(text + '\n')

output_txt_path

!pip install spacy
!pip install scispacy
!pip install transformers

tokenizer = AutoTokenizer.from_pretrained("dmis-lab/biobert-base-cased-v1.2")
model = AutoModel.from_pretrained("dmis-lab/biobert-base-cased-v1.2")

from transformers import AutoTokenizer
from collections import Counter

# Function to count unique tokens in text and return the top 30 most common tokens
def count_unique_tokens(text, model="bert-base-uncased"):
    # Load the tokenizer for the specified model
    tokenizer = AutoTokenizer.from_pretrained(model)

    # Tokenize the text
    tokens = tokenizer.tokenize(text)

    # Count occurrences of each token
    token_counts = Counter(tokens)

    # Return the top 30 most common tokens
    return token_counts.most_common(30)

with open("extracted_texts.txt", "r", encoding="utf-8") as file:
    text_data = file.read()

top_30_tokens = count_unique_tokens(text_data)
print(top_30_tokens)

