# 2048-game-automator.py
# Description: Automates playing the 2048 game by randomly sending keystrokes for directional movements.
# It automatically accepts cookies, detects when the game is over, displays the score, and restarts the game.

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random

# Initialize the Selenium WebDriver for Safari
driver = webdriver.Safari()
driver.get("https://gabrielecirulli.github.io/2048/")

# Attempt to accept cookies to ensure the game is interactable
try:
    wait = WebDriverWait(driver, 20)
    agree_button = wait.until(EC.element_to_be_clickable((By.ID, "ez-accept-all")))
    agree_button.click()
    time.sleep(2)  # Wait for the page to become interactable after accepting cookies
except Exception as e:
    print(f"Could not click the accept cookies button. Error: {e}")

# Main loop to play the game
try:
    # Focus the game container to send keystrokes
    game_container = driver.find_element(By.CLASS_NAME, "game-container")
    game_container.click()

    # List of possible keystrokes to control the game
    key_list = [Keys.DOWN, Keys.UP, Keys.LEFT, Keys.RIGHT]

    while True:
        # Check for the game over message
        game_over_elements = driver.find_elements(By.CSS_SELECTOR, ".game-message.game-over")

        if game_over_elements:
            print("Game Over. Trying again.")
            score_element = driver.find_element(By.CLASS_NAME, "score-container")
            print(f"Score: {score_element.text.strip()}")  # Display the final score

            # Click the retry button to start a new game
            retry_button = driver.find_element(By.CLASS_NAME, "retry-button")
            retry_button.click()
            time.sleep(2)  # Wait before starting a new game
            continue

        # Randomly choose a direction to move and send the keystroke
        random_key = random.choice(key_list)
        game_container.send_keys(random_key)
except Exception as e:
    print(f"Could not interact with the game. Error: {e}")
finally:
    driver.quit()  # Ensure the driver is closed after the script ends or encounters an error
