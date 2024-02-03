# excel-text-to-spreadsheet-converter.py
# Description: Reads content from specified text files and populates an Excel spreadsheet,
# placing the content of each text file into a separate column.
# Ideal for consolidating textual data into a single, organized format for analysis or review.

import openpyxl
import os

# Function to read content from a text file
def read_file(file_path):
    with open(file_path, 'r') as open_file:
        return open_file.readlines()

# Create a new workbook and select the active sheet
wb = openpyxl.Workbook()
sheet = wb.active
sheet.title = ""

# List of text file paths (replace these paths with your actual file paths)
file_paths = [
    "path/to/your/testfile1.txt",
    "path/to/your/testfile2.txt",
    "path/to/your/testfile3.txt"
]

# Dictionary to hold text content from files
text_from_files = {}

# Read content from each file and store it in the dictionary
for file_path in file_paths:
    text_from_files[file_path] = read_file(file_path)

# Populate the spreadsheet with content from each text file
col_index = 1
for _, lines in text_from_files.items():
    row_index = 1
    for line in lines:
        # Write each line to the spreadsheet, removing trailing newlines
        sheet.cell(row=row_index, column=col_index, value=line.strip())
        row_index += 1
    col_index += 1

# Save the populated workbook to a new Excel file
output_filename = 'textfiles_consolidated.xlsx'
wb.save(output_filename)
print(f'Spreadsheet saved as {output_filename}.')
