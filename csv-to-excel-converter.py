# csv-to-excel-converter.py
# Description: Reads data from a specified CSV file and writes it to a new Excel spreadsheet,
# maintaining the original structure and content.
# Ideal for converting CSV data for use in Excel-compatible applications.

import csv
import openpyxl

# Specify the path to your CSV file
csv_filepath = ""  # Replace with your actual CSV file path

# Open and read the CSV file
with open(csv_filepath, 'r', encoding='utf-8') as file:
    csv_reader = csv.reader(file, delimiter=';')  # Read data with specified delimiter
    csv_data = list(csv_reader)  # Convert CSV data to a list

# Create a new Excel workbook and select the active worksheet
wb = openpyxl.Workbook()
sheet = wb.active

# Iterate over the CSV data and write each value to the Excel sheet
for row_index, row in enumerate(csv_data, start=1):
    for col_index, value in enumerate(row, start=1):
        # Write data to corresponding cell in the Excel sheet
        sheet.cell(row=row_index, column=col_index, value=value)

# Define the name for the output Excel file
output_excel_name = 'csv-to-excel.xlsx'

# Save the Excel workbook to the specified file
wb.save(output_excel_name)
print(f'Spreadsheet saved as {output_excel_name}')
