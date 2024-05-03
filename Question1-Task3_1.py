
# Question 1
# Task 3: Programming and Research
    # 3.1: Using any in-built library present in Python, count the occurrences of the words in the text (.txt)
    # and give the ‘Top 30’ most common words. And store the ‘Top 30’ common words and their counts into a CSV file.

import pandas as pd
from collections import Counter
import csv

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
