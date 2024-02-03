# xkcd-comic-downloader.py
# Description: Downloads all XKCD comics by navigating from the latest comic to the first one.
# Saves each comic image in an 'xkcd' directory within the current working directory.

import requests
import os
import bs4

url = 'https://xkcd.com'  # Starting URL for the latest XKCD comic
os.makedirs('xkcd', exist_ok=True)  # Creates a directory for storing comics if it doesn't already exist

while not url.endswith('#'):  # The last comic's 'Prev' link is '#'
    print(f'Downloading page {url}...')
    response = requests.get(url)
    response.raise_for_status()

    soup = bs4.BeautifulSoup(response.text, 'html.parser')

    # Attempt to find the URL of the comic image
    comic_element = soup.select('#comic img')
    if not comic_element:
        print('Could not find comic image on the page.')
    else:
        comic_url = 'https:' + comic_element[0].get('src')
        print(f'Downloading image {comic_url}...')
        response = requests.get(comic_url)
        response.raise_for_status()

        # Save the comic image to the 'xkcd' directory
        with open(os.path.join('xkcd', os.path.basename(comic_url)), 'wb') as image_file:
            for chunk in response.iter_content(100000):
                image_file.write(chunk)

    # Find and set the URL for the 'Prev' button to continue downloading
    prev_link = soup.select('a[rel="prev"]')[0]
    url = 'https://xkcd.com' + prev_link.get('href')

print('Finished downloading all XKCD comics.')
