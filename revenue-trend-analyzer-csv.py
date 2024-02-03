# revenue-trend-analyzer-csv.py
# Description: Analyzes revenue data from CSV files for specified NAICS codes and years, compares the revenue trends,
# and generates a report highlighting these trends and variations.
# Note: The program written for a specific set of csv files.

import csv
import os
import re
from collections import defaultdict

# Function to write the analysis results to a text file
def write_to_file(filename, data):
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(data)

# Function to format the comparison results for output
def prepare_data_for_output(comparison_results):
    output_data = []
    for naics_desc, data_list in comparison_results.items():
        output_data.append(f"NAICS Description: {naics_desc}\n" + "="*50 + "\n")
        for data in data_list:
            revenue_2012 = data['2012 Revenue']
            revenue_2011 = data['2011 Revenue']
            variation_2010 = data['2010 Coefficient of Variation']
            source_file = data['Source File']

            trend = "remained the same"
            if revenue_2012 is not None and revenue_2011 is not None:
                if revenue_2012 > revenue_2011:
                    trend = "increased"
                elif revenue_2012 < revenue_2011:
                    trend = "decreased"

            output_data.append(f"Source File: {source_file}, Revenue {trend} from 2011 to 2012. 2010 Coefficient of Variation: {variation_2010}\n")
            output_data.append("-"*50 + "\n")

    return ''.join(output_data)

# Function to safely convert string to float, handling commas and invalid values
def safe_convert_to_float(value):
    try:
        return float(value.replace(',', ''))
    except ValueError:
        return None

# Function to normalize text for consistent comparison
def normalize_text(text):
    return ' '.join(text.split()).strip().lower()

# Main function to compare data across CSV files for specified NAICS codes
def compare_data(directory, naics_codes, columns):
    data_comparison = defaultdict(list)
    naics_codes_normalized = [normalize_text(code) for code in naics_codes]

    for filename in os.listdir(directory):
        if filename.endswith('.csv'):
            filepath = os.path.join(directory, filename)
            with open(filepath, 'r', encoding='utf-8') as file:
                reader = csv.DictReader(file)

                for row in reader:
                    naics_desc = normalize_text(row['NAICS Description'])
                    if naics_desc in naics_codes_normalized:
                        data = {column: safe_convert_to_float(row[column]) for column in columns}
                        data['Source File'] = filename
                        data_comparison[naics_desc].append(data)

    return data_comparison

# Path to the directory containing the CSV files
directory = ""  # Replace with your actual directory path
naics_codes = ["Computer Systems Design and Related Services", "Motion Picture and Video Exhibition"]
columns = ["2012 Revenue", "2011 Revenue", "2010 Coefficient of Variation"]

# Perform the data comparison and generate the output report
comparison_results = compare_data(directory, naics_codes, columns)
output_text = prepare_data_for_output(comparison_results)
write_to_file("comparison_results.txt", output_text)
