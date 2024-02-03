# data-validator.py
# Description: Validates data in a CSV file, checking for correct data types and formats.
# Reports any inconsistencies or errors found, such as invalid integer or float values, and incorrect email formats.

import csv
import os
import re

# Function to check if a value can be converted to an integer
def is_int(value):
    try:
        int(value)
        return True
    except ValueError:
        return False

# Function to check if a value can be converted to a float
def is_float(value):
    try:
        float(value)
        return True
    except ValueError:
        return False

# Function to validate an email address using regex
def is_valid_email(email):
    email_regex = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
    return re.match(email_regex, email) is not None

# Replace with the path to your CSV file
csv_file_path = ""

# Open and read the CSV file
with open(csv_file_path, 'r', encoding='utf-8') as file:
    csv_reader = csv.reader(file)
    header = next(csv_reader)  # Assume the first row is the header
    data = list(csv_reader)  # Convert the rest of the rows to a list

# List to collect error messages
errors = []
expected_field_count = 4  # Expected number of fields in each row

# Validate each row of the CSV file
for row_index, row in enumerate(data, start=2):  # Start counting rows from 2
    if len(row) != expected_field_count:
        errors.append(f"Row {row_index} has inconsistent field count.")
        continue

    name, age, email, salary = row  # Unpack row values

    # Check for missing required fields
    if not all(row):
        errors.append(f"Row {row_index} is missing required field(s).")

    # Validate data types and formats
    if not is_int(age):
        errors.append(f"Invalid age value in row {row_index}.")
    if not is_float(salary):
        errors.append(f"Invalid salary value in row {row_index}.")
    if not is_valid_email(email):
        errors.append(f"Invalid email format in row {row_index}.")

# Print out any errors found during validation
for error in errors:
    print(error)
