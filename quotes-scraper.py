# quotes-scraper.py
# Description: Iterates through the pages of the "Quotes to Scrape" website, downloading each page's content.
# The script is intended to scrape and potentially save quotes, navigating through the site using the 'Next' link.

import requests
import os
import bs4
from urllib.parse import urljoin

# Starting URL for the scraping process
url = 'http://quotes.toscrape.com'

# Ensure the directory for saving data exists
os.makedirs('quotes', exist_ok=True)

while True:
    # Attempt to download the current page
    print(f'Downloading page {url}...')
    try:
        response = requests.get(url)
        response.raise_for_status()  # Check for errors
    except requests.RequestException as e:
        print(f"An error occurred: {e}")
        break

    soup = bs4.BeautifulSoup(response.text, 'html.parser')

    # Intended to find and process each quote on the page here
    # For demonstration, print the current page's URL
    print(f'Processing content from {url}')

    # Find the 'Next' button's link to continue to the next page
    next_link = soup.find('a', text='Next')
    if not next_link:
        print('Reached the last page.')
        break  # Exit the loop if no 'Next' link is found
    url = urljoin(url, next_link['href'])  # Prepare the URL for the next page

print('Finished downloading all pages.')
