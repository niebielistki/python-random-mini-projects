# pdf-page-reorganizer.py
# Description: Reorders selected pages in a PDF document according to a specified sequence and saves
# the reordered version as a new PDF file. Useful for customizing the order of pages in meeting minutes or reports.

import PyPDF2

# Initialize PDF reader for the source document
pdfReader = PyPDF2.PdfReader("")  # Replace with the path to your PDF

# Specify the new order for pages (note: page numbering starts at 1)
pages_to_reorder = [2, 1, 3, 6, 5, 4]

# Initialize PDF writer for the output document
pdfWriter = PyPDF2.PdfWriter()

# Reorder pages and add them to the output PDF
for pageNum in pages_to_reorder:
    # Adjust page number to match Python's 0-based indexing
    adjustedPageNum = pageNum - 1
    page = pdfReader.pages[adjustedPageNum]
    pdfWriter.add_page(page)

# Save the reordered PDF to a new file
with open('reordered_pdf.pdf', 'wb') as outputFile:
    pdfWriter.write(outputFile)
print("Reordered PDF has been created successfully.")
