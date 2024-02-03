# value-occurrence-tracker-csv.py
# Description: Searches for specified values within all CSV files in a given directory and counts their occurrences,
# providing a summary of findings. Useful for data auditing or content discovery across large datasets.
# Note: The program written for a specific set of csv files.

import os
import pandas as pd

# Path to the directory containing CSV files
directory = ""  # Replace with your actual directory path

# List of specific values to search for within the CSV files
values_to_search = [
    "Computer Systems Design and Related Services",
    "Motion Picture and Video Exhibition",
    "Museums, Historical Sites, and Similar Institutions",
    "Music Publishers",
    "Book Publishers"
]

# Initialize a dictionary to count occurrences of each value
values_count = {value: 0 for value in values_to_search}

# Function to search for the values within a dataframe and update their occurrence count
def search_values_in_dataframe(df, values):
    found_values = {value: 'NO' for value in values}
    for column in df.columns:
        for value in values:
            if df[column].astype(str).str.contains(value, regex=False).any():
                found_values[value] = f'YES (Column: {column})'
                values_count[value] += 1
    return found_values

# Process each CSV file in the specified directory
for filename in os.listdir(directory):
    if filename.endswith('.csv'):
        file_path = os.path.join(directory, filename)
        df = pd.read_csv(file_path)

        print(f'Filename: {filename}')
        found_values = search_values_in_dataframe(df, values_to_search)
        for value, presence in found_values.items():
            print(f'{value} - {presence}')
        print('...')

# Print a summary of the search results, sorted by the number of appearances
print("\nSummary:")
sorted_values_count = sorted(values_count.items(), key=lambda x: x[1], reverse=True)
for value, count in sorted_values_count:
    print(f'{value}: Appearances - {count}')
