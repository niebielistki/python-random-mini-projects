# mad-libs-generator.py
# Description: Reads a "Mad Libs" template from a file, prompts the user to replace placeholders (adjective, noun, adverb, verb)
# with their own words, and saves the modified story to a new file. Enhances reading and writing skills in a fun way.

import re

# List of placeholder words in the Mad Libs template
placeholders = ['adjective', 'noun', 'adverb', 'verb']

# Function to replace placeholders with user input
def replace_placeholder(match):
    word = match.group().lower()
    if word in placeholders:
        return input(f'Please enter an {word}:\n')  # Prompt for user input
    return word  # Return the original word if it's not a placeholder

# Attempt to open and read the Mad Libs template file
try:
    with open("path/to/your/madlibs_test.txt", 'r') as file:  # Replace with your file path
        text = file.read()
    print("Original text:\n", text)

    # Use regex to find and replace placeholders with user input
    result_text = re.sub(r'\b(?:' + '|'.join(placeholders) + r')\b', replace_placeholder, text, flags=re.IGNORECASE)
    print("\nCompleted story:\n", result_text)

    # Save the completed story to a new file
    with open('madlibs_completed.txt', 'w') as output_file:
        output_file.write(result_text)
except FileNotFoundError:
    print("The file was not found.")
