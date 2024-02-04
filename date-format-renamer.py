# date-format-renamer.py
# Description: Searches for filenames in a specified directory that contain dates in the American MM-DD-YYYY format
# and renames them to the European DD-MM-YYYY format. Useful for standardizing date formats across files.

import shutil
import os
import re

# Regex pattern to identify American date format in filenames
date_pattern = re.compile(r"""^(.*?)  # all text before the date
       ((0|1)?\d)-                    # month
       ((0|1|2|3)?\d)-                # day
       ((19|20)\d\d)                  # year
       (.*?)$                         # all text after the date
       """, re.VERBOSE)

# Define the directory containing files to be renamed
folder_path = "path/to/your/folder"  # Replace with the path to your target folder

# Iterate over each file in the directory
for filename in os.listdir(folder_path):
    mo = date_pattern.search(filename)

    # Skip files without a date
    if mo is None:
        continue

    # Extract the various parts of the filename
    before_part = mo.group(1)
    month_part  = mo.group(2)
    day_part    = mo.group(4)
    year_part   = mo.group(6)
    after_part  = mo.group(8)

    # Construct the European-style filename
    euro_filename = f"{before_part}{day_part}-{month_part}-{year_part}{after_part}"

    # Full paths for the original and new filenames
    old_filepath = os.path.join(folder_path, filename)
    new_filepath = os.path.join(folder_path, euro_filename)

    # Rename the file
    print(f'Renaming "{filename}" to "{euro_filename}"...')
    shutil.move(old_filepath, new_filepath)
