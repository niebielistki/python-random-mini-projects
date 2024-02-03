# open-map-from-address.py
# Description: Opens a Google Maps page in the web browser for a specific address.
# The address is taken from the command line if provided; otherwise, it uses the address copied to the clipboard.

import webbrowser
import sys
import pyperclip

# Check if an address was provided as a command-line argument
if len(sys.argv) > 1:
    # Concatenate the command line arguments to form the address
    address = ' '.join(sys.argv[1:])
else:
    # If no command-line argument, use the address from the clipboard
    address = pyperclip.paste()

# Open the web browser to the Google Maps page for the specified address
webbrowser.open('https://www.google.com/maps/place/' + address)
