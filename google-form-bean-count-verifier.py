# google-form-bean-count-verifier.py
# Description: Verifies the calculations in a Google Sheets spreadsheet that tracks the number
# of beans per jar, the number of jars, and the total beans. It checks each row for consistency in these
# calculations and identifies the first row where the data does not match.

import ezsheets

# Initialize access to the specific Google Sheets spreadsheet by its ID
ss = ezsheets.Spreadsheet('')  # Replace with your actual spreadsheet ID

# Access the first sheet in the spreadsheet
sheet = ss[0]

# Iterate through each row in the sheet starting from the second row
for rowNum in range(2, sheet.rowCount + 1):
    row = sheet.getRow(rowNum)  # Retrieve data from the current row

    # Check if the row contains data for beans per jar, number of jars, and total beans
    if row[0] and row[1] and row[2]:
        # Convert row data to integers for calculation
        beans_per_jar = int(row[0])
        jars = int(row[1])
        total_beans = int(row[2])

        # Verify if the calculated total matches the provided total beans
        if beans_per_jar * jars != total_beans:
            print(f"Mistake found in row: {rowNum}.")
            break  # Exit the loop upon finding the first mistake
