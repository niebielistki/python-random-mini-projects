# google-form-email-extractor.py
# Description: Extracts email addresses from a Google Sheets document and saves them to a text file.
# Validates email formats using a regular expression.

import ezsheets
import re

# Initialize access to the specified Google Sheets spreadsheet by its ID
ss = ezsheets.Spreadsheet('')  # Replace with your spreadsheet ID

# Access the first sheet in the spreadsheet, assuming it contains the form responses
form = ss[0]

# Compile a regular expression pattern for validating email addresses
re_email = re.compile('^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')

emails = []  # List to store found email addresses

# Iterate through each row in the sheet, starting from the second row
for rowIndex in range(2, form.rowCount + 1):
    row = form.getRow(rowIndex)  # Retrieve the current row
    for cell in row:
        if re_email.match(cell):  # Check if the cell contains a valid email address
            emails.append(cell)  # Add valid email addresses to the list

# Save the extracted email addresses to a text file
with open('emails.txt', 'w') as file:
    for email in emails:
        file.write(email + '\n')

print('All email addresses were saved in a file: emails.txt')
