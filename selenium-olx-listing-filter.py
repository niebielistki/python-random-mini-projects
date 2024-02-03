# selenium-olx-listing-filter.py
# Description: Automates searching for items on OLX within a specified price range and based on a list of allowed and restricted keywords.
# Listings matching the criteria are opened in new tabs for review. The script navigates through search result pages until no further pages are available.

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import time

# Function to check if a listing's title matches the allowed and restricted keywords
def check_keywords(title, allowed_keywords, restricted_keywords):
    """Checks if the title contains any allowed keywords and no restricted keywords."""
    return any(keyword.lower() in title for keyword in allowed_keywords) and \
           not any(keyword.lower() in title for keyword in restricted_keywords)

# Initialize WebDriver
driver = webdriver.Safari()
driver.get("https://www.olx.pl/")

# Accept cookies if the button is present
try:
    accept_cookies = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "onetrust-accept-btn-handler"))
    )
    accept_cookies.click()
except Exception:
    print("Could not click the accept cookies button.")

# Perform a search query
search_box = driver.find_element(By.ID, "headerSearch")
search_box.send_keys("kożuch" + Keys.RETURN)  # Replace "kożuch" with your search term
time.sleep(5)

# Set a maximum price limit
max_price_box = driver.find_element(By.NAME, "range-to-input")
max_price_box.send_keys("350" + Keys.RETURN)  # Adjust "350" to your max price
time.sleep(5)

# Define allowed and restricted keywords
allowed_keywords = ["naturalny", "skóra", "skórzany", "skóry", "naturalna", "naturalne", "licowa",
                     "skórzana", "owczy", "ze skóry", "wykończenie", "ocieplany", "ocieplana"]
restricted_keywords = ["Zara", "H&M", "Stradivarius", "eko", "ekologiczna", "sztuczne", "sztuczny"]

page_number = 1

# Iterate through search result pages and process listings
while True:
    print(f"Processing page {page_number}")

    try:
        items = driver.find_elements(By.XPATH, "//h6[contains(@class, 'css-16v5mdi')]")

        for index, item in enumerate(items):
            title = item.text.lower()

            if check_keywords(title, allowed_keywords, restricted_keywords):
                # Open listings that match the criteria in new tabs
                parent_item = item.find_element(By.XPATH, "./ancestor::a")
                link = parent_item.get_attribute("href")
                print(f"Opening new tab for {link}")
                driver.execute_script(f"window.open('{link}', '_blank')")

        # Navigate to the next page if available
        try:
            next_page_btn = driver.find_element(By.CSS_SELECTOR, "a[data-testid='pagination-forward']")
            next_page_btn.click()
            time.sleep(5)
        except NoSuchElementException:
            print("Reached the last page.")
            break

        page_number += 1

    except Exception as e:
        print(f"An error occurred: {e}")
        break

    finally:
        driver.quit()  # Close the driver when done or in case of an error
