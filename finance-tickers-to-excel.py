# finance-tickers-to-excel.py
# Description: Fetches the list of trending stock tickers from Yahoo Finance and saves the data into an Excel spreadsheet.
# It captures the ticker symbols and related data, excluding the last three columns of additional metrics.

import requests
from bs4 import BeautifulSoup
from openpyxl import Workbook

# Target URL containing the trending stock tickers
url = 'https://finance.yahoo.com/trending-tickers'

# Send a request to the URL
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content
    soup = BeautifulSoup(response.text, 'html.parser')
    # Find the table containing the trending tickers
    table = soup.find('table', {'class': 'W(100%)'})

    # Proceed if the table was found
    if table:
        # Initialize a new Excel workbook and select the active sheet
        workbook = Workbook()
        sheet = workbook.active

        # Iterate through each row in the table, excluding the header and the last three columns
        for row in table.find_all('tr')[1:]:
            # Extract text from each cell in the row
            row_data = [cell.get_text() for cell in row.find_all('td')[:-3]]
            # Append the row data to the sheet
            sheet.append(row_data)

        # Save the workbook with the trending tickers data
        workbook.save('trending_tickers.xlsx')
        print("Trending stock tickers have been saved to 'trending_tickers.xlsx'.")
    else:
        print('Table not found in the HTML content.')
else:
    print('Failed to retrieve the webpage.')
