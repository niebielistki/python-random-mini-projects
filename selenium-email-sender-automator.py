# selenium-email-sender-automator.py
# Description: Automates the process of logging into the Mail.com website and sending an email using credentials and email content
# provided by the user via the command line. Validates email formats and message content before proceeding.

import sys
import re
import getpass
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Function to validate the email address format
def validate_email(email):
    """Checks if the provided email address matches the standard email format."""
    email_regex = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
    return re.match(email_regex, email) is not None

# Function to validate the message content
def validate_message(message):
    """Checks if the provided message is not empty or just whitespace."""
    return bool(message and message.strip())

# Verify correct usage and command line arguments
if len(sys.argv) != 3:
    print(f"Usage: python {sys.argv[0]} [recipient_email] [message]")
    sys.exit(1)

recipient_email = sys.argv[1]
message_content = sys.argv[2]

sender_email = input("Enter your Mail.com email address: ")
password = getpass.getpass("Enter your Mail.com password: ")

# Validate provided email addresses and message
if not validate_email(recipient_email):
    print("Invalid recipient email address format. Exiting.")
    sys.exit(1)

if not validate_email(sender_email):
    print("Invalid sender email address format. Exiting.")
    sys.exit(1)

if not validate_message(message_content):
    print("Invalid or empty message content. Exiting.")
    sys.exit(1)

# Initialize WebDriver
driver = webdriver.Safari()
driver.get("https://www.mail.com")

# Navigate to the login page
try:
    login_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "login-button"))
    )
    login_button.click()
except Exception as e:
    print("Failed to navigate to the login page.")
    driver.quit()
    sys.exit(1)

# The script would continue to fill in the login form, navigate to the email composition page, and send an email.
# This example stops here for brevity and because further steps would require interacting with Mail.com's specific elements and forms.
