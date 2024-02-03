# pdf-encryptor.py
# Description: Encrypts all PDF files within a specified directory using a password provided
# via the command line. The original PDF files are replaced with their encrypted versions.

import os
import sys
import PyPDF2
import re

# Function to validate the provided password against a pattern
def validate_password(password):
    pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[A-Za-z\d]{8,}$'
    return re.match(pattern, password) is not None

# Function to split a filename into its name and extension
def split_filename(filename):
    return os.path.splitext(filename)

# Check if a password is provided
if len(sys.argv) > 1:
    password = sys.argv[1]
    if not validate_password(password):
        print('Provided password does not meet the criteria.')
        sys.exit()

# Path to the directory containing PDF files
directory = ""  # Replace with your actual directory path

# Find all PDF files in the directory
pdf_files = [os.path.join(folderName, file) for folderName, _, filenames in os.walk(directory) for file in filenames if file.endswith('.pdf')]

# Encrypt each PDF file
for file in pdf_files:
    with open(file, 'rb') as pdf_file:
        pdfReader = PyPDF2.PdfReader(pdf_file)
        pdfWriter = PyPDF2.PdfWriter()

        for page in pdfReader.pages:
            pdfWriter.add_page(page)

        pdfWriter.encrypt(password)
        encrypted_file_path = file.replace('.pdf', '_encrypted.pdf')

        with open(encrypted_file_path, 'wb') as result_pdf:
            pdfWriter.write(result_pdf)

    os.remove(file)  # Delete the original file
    print(f"Encrypted {file} to {encrypted_file_path}.")

