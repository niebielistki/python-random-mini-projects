# selenium-image-downloader.py
# Description: Automates searching for and downloading images from Imgur based on a specified search term.
# Saves the first five search result images locally. Utilizes Selenium for web navigation and interaction.

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.keys import Keys
import time
import requests

# Function to download an image from a given URL
def download_image(image_url, image_name):
    """Downloads an image from the given URL and saves it with the specified image name."""
    response = requests.get(image_url)
    if response.status_code == 200:
        with open(image_name, 'wb') as file:
            file.write(response.content)

# Initialize the WebDriver
driver = webdriver.Safari()
driver.get("https://imgur.com")

try:
    # Wait for the search box to become available and enter the search term
    search_box = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CLASS_NAME, "Searchbar-textInput")))
    search_box.send_keys("cars" + Keys.RETURN)  # Replace "cars" with your search term
    time.sleep(5)  # Wait for search results to load

    # Find the first five image links from the search results
    image_links = driver.find_elements(By.CSS_SELECTOR, "a.image-list-link")[:5]

    original_window = driver.current_window_handle

    # Loop through the found image links
    for i, link in enumerate(image_links):
        # Open each image link in a new tab
        driver.execute_script("window.open(arguments[0], '_blank');", link.get_attribute('href'))
        time.sleep(2)

        # Switch to the new tab
        driver.switch_to.window(driver.window_handles[-1])

        try:
            # Wait for the image to load and retrieve its URL
            image_element = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "img.post-image-placeholder"))
            )
            image_url = image_element.get_attribute("src")

            # Download the image
            download_image(image_url, f"image_{i}.jpg")
        except (NoSuchElementException, TimeoutException):
            print(f"Image {i} could not be found or took too long to load.")
        finally:
            driver.close()  # Close the new tab
            driver.switch_to.window(original_window)  # Switch back to the original tab

        time.sleep(1)
except Exception as e:
    print(f"An unexpected error occurred: {e}")
finally:
    driver.quit()  # Ensure the driver is closed properly
