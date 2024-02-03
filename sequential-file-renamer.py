# sequential-file-renamer.py
# Description: Renames files in a specified directory to ensure a sequential numbering scheme.
# Targets files named with a 'spamXXX' pattern, where XXX is a number, and renames them starting from 'spam001.txt' onwards.

import os
import re

# Define the target directory for renaming files
directory = ""  # Replace with the actual path to your folder

def extract_number(filename):
    """Extracts the numeric part from filenames following the 'spamXXX' pattern."""
    pattern = re.compile(r'spam(\d{3})')
    match = re.search(pattern, filename)
    return int(match.group(1)) if match else None

def sort_files(files_list):
    """Sorts a list of filenames based on their numeric part extracted from the 'spamXXX' pattern."""
    return sorted(files_list, key=extract_number)

def rename_files(folder_path):
    """Renames files in the specified folder to maintain a sequential numbering without gaps."""
    matching_files = [f for f in os.listdir(folder_path) if re.match(r'spam\d{3}', f)]
    sorted_files = sort_files(matching_files)

    for i, filename in enumerate(sorted_files, start=1):
        new_filename = f'spam{i:03d}.txt'
        os.rename(os.path.join(folder_path, filename), os.path.join(folder_path, new_filename))
        print(f'Renamed {filename} to {new_filename}')

# Call the rename_files function to start the renaming process
rename_files(directory)
