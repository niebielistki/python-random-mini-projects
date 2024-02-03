# create-pdf-with-target-pages.py
# Description: Scans a PDF document for pages containing monetary values (formatted as $amount)
# and creates a new PDF document containing only those pages.
# Useful for extracting financial information from meeting minutes or reports.

import PyPDF2
import re

# Regular expression pattern to match monetary values
pattern = re.compile(r'\$[0-9,]+(?:\.\d{2})?')

# Initialize PDF reader for the source document
pdfReader = PyPDF2.PdfReader()  # Replace with the path to your PDF

# Initialize PDF writer for the output document
pdfWriter = PyPDF2.PdfWriter()

try:
    # Iterate through each page in the source PDF
    for page_num in range(len(pdfReader.pages)):
        page = pdfReader.pages[page_num]
        page_content = page.extract_text()  # Extract text content from the page
        matches = pattern.findall(page_content)  # Find all monetary values on the page

        if matches:  # If monetary values are found, add the page to the output document
            pdfWriter.add_page(page)

    # Save the output PDF with pages containing monetary values
    with open('pdf-with-target-pages.pdf', 'wb') as outputFile:
        pdfWriter.write(outputFile)
    print('PDF containing pages with financial information has been created successfully.')
except Exception as e:
    print(f'An error occurred: {e}')
