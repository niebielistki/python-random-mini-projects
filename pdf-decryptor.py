# pdf-decryptor.py
# Description: Finds all encrypted PDFs in a directory and its subfolders, then creates a decrypted copy using a provided password. Encrypted files are identified by a specific suffix.

import os
import fitz  # PyMuPDF

# Path to the directory containing encrypted PDF files
directory = ""  # Replace with your actual directory path
password = "Pass1234"  # The password used for decryption

# Decrypt each encrypted PDF file
for folderName, subfolders, filenames in os.walk(directory):
    for filename in filenames:
        if filename.endswith('_encrypted.pdf'):
            file_path = os.path.join(folderName, filename)
            new_file_name = file_path.replace('_encrypted.pdf', '_decrypted.pdf')

            try:
                with fitz.open(file_path) as doc:
                    if doc.authenticate(password):
                        doc.save(new_file_name)
                        print(f"Decrypted and saved: {new_file_name}")
                    else:
                        print(f"Failed to decrypt {file_path}: Incorrect password")
            except Exception as e:
                print(f"Failed to decrypt {file_path}: {e}")
