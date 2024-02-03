# selective-file-copy.py
# Description: Searches a specified directory for files with certain extensions and copies those files to a designated destination folder.
# Designed to help with organizing or backing up specific types of files.

import os
import shutil

# Define the source and destination directories
source_directory = "path/to/source/directory"  # Replace with your source directory path
destination_directory = "path/to/destination/directory"  # Replace with your destination directory path

# List of file extensions to be copied
extensions_to_copy = ['.jpg', '.pdf']

# Collect files to copy
files_to_copy = []
for dirpath, dirnames, filenames in os.walk(source_directory):
    for filename in filenames:
        if os.path.splitext(filename)[1] in extensions_to_copy:
            files_to_copy.append(os.path.join(dirpath, filename))

# Attempt to copy the selected files to the destination directory
for filepath in files_to_copy:
    try:
        shutil.copy(filepath, destination_directory)
    except IOError as e:
        print(f"Unable to copy file {filepath} to {destination_directory}. {e}")

print(f'Finished copying selected files to the destination folder: {destination_directory}')
