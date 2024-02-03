# pdf-password-breaker.py
# Description: Attempts to decrypt an encrypted PDF file by trying passwords from a specified dictionary text file.
# Reports when the password is found or if it fails to find it within the dictionary.

import PyPDF2

# Load potential passwords from a dictionary file
words = []
dictionary_path = ""  # Replace with your actual dictionary file path
with open(dictionary_path, 'r') as file:
    words = [line.strip() for line in file]

# Specify the path to the encrypted PDF file
pdf_file_path = ""  # Replace with your actual PDF file path
pdfReader = PyPDF2.PdfReader(pdf_file_path)

# Check if the PDF is encrypted and attempt to decrypt it
if not pdfReader.is_encrypted:
    print("The PDF is not encrypted. No need to decrypt.")
else:
    print("Attempting to decrypt the PDF...")
    password_found = False
    for word in words:
        if pdfReader.decrypt(word.lower()) or pdfReader.decrypt(word.upper()):
            print(f"Password found: {word}")
            password_found = True
            break

    if not password_found:
        print("Password not found in the dictionary.")
