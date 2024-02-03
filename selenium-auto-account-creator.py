# selenium-auto-account-creator.py
# Description: Automates the process of creating a new account on a specified forum by collecting user input for username, password,
# email, and a security question answer, then interacts with the web page to input and submit the account creation form.

import sys
import re
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
import time


# Collects necessary user input for account creation
def collect_user_input():
    print('Please complete the information needed to create a new account.')
    username = input('Your username: ')
    while len(username) < 5:
        print("Username must be at least 5 characters long.")
        username = input('Your username: ')
    password = input('Your password: ')
    while len(password) < 8:
        print("Password must be at least 8 characters long.")
        password = input('Your password: ')
    email = input('Your e-mail: ')
    while "@" not in email or "." not in email:
        print("Please enter a valid email address.")
        email = input('Your e-mail: ')
    print(
        'Answer to the security question: The king who was victorious in the battle against the Teutonic Knights in 1410?')
    correct_answers = ['władysław jagiełło', 'wladyslaw jagiello']
    user_answer = input().lower()
    while user_answer not in correct_answers:
        print('Incorrect! Guess again.')
        user_answer = input().lower()
    print('Everything is correct. Your account will be created in a moment.')
    return username, password, email, user_answer


# Collect user information
username, password, email, question = collect_user_input()

# Initialize WebDriver and navigate to the specified forum page
driver = webdriver.Safari()
driver.get("https://renault.auto.com.pl/forum/index.php")

try:
    # Handle cookie and consent forms
    wait = WebDriverWait(driver, 20)
    agree_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "css-oucen6")))
    agree_button.click()
    time.sleep(2)

    # Navigate to the registration page
    register_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "fsprite-icon-mini-register")))
    register_button.click()
    time.sleep(5)
    accept_link = wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//a[@class='genmed' and contains(@href, 'profile.php?mode=register&agreed=true')]")))
    accept_link.click()

    # Fill in the registration form with collected user input
    username_elem = wait.until(EC.presence_of_element_located((By.NAME, 'username')))
    username_elem.send_keys(username)
    password_elem = wait.until(EC.presence_of_element_located((By.NAME, 'new_password')))
    password_elem.send_keys(password)
    confirm_password_elem = wait.until(EC.presence_of_element_located((By.NAME, 'password_confirm')))
    confirm_password_elem.send_keys(password)
    email_elem = wait.until(EC.presence_of_element_located((By.NAME, 'email')))
    email_elem.send_keys(email)
    question_elem = wait.until(EC.presence_of_element_located((By.NAME, 'confirm_sec_answ')))
    question_elem.send_keys(question)

except TimeoutException:
    print("Timed out waiting for page elements to load.")
except NoSuchElementException:
    print("Required page element not found.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
finally:
    # Ensure the driver is closed properly after execution or in case of error
    driver.quit()
