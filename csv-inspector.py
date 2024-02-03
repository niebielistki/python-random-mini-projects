# csv-inspector.py
# Description: Inspects and displays the contents of all CSV files in a specified directory, highlighting empty files.
# Usage: Ideal for data analysts or developers needing to quickly verify CSV contents within a project folder.

import os
import csv

# Specify the directory containing the CSV files (replace with your actual folder path)
folder_path = ""  # Replace with your folder path

# Loop through each file in the specified directory
for filename in os.listdir(folder_path):
    if filename.endswith('.csv'):
        print(f"File: {filename}")

        # Construct file path and open the CSV file
        with open(os.path.join(folder_path, filename), 'r', encoding='utf-8') as file:
            csv_reader = csv.reader(file, delimiter=';')
            is_empty = True  # Flag to detect empty files

            # Iterate through rows in the CSV file
            for row in csv_reader:
                # Ensure the row contains non-whitespace data before printing
                if any(field.strip() for field in row):
                    print(';'.join(row))
                    is_empty = False  # File contains data

            # Notify if the file has no data
            if is_empty:
                print("(This file is empty)")

        print("\n")  # Separate output between files for readability
