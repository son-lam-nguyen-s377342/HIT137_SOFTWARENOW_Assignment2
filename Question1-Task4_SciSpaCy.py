
# Task 4: Named-Entity Recognition (NER)
# Extract the ‘diseases’, and ‘drugs’ entities in the ‘.txt file’ separately using ‘en_core_sci_sm’/’en_ner_bc5cdr_md’
# and biobert. And compare the differences between the two models (Example: Total entities detected by both of them,
# what’s the difference, check for most common words, and check the difference.)

import spacy
import csv
from collections import Counter
from tqdm import tqdm

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