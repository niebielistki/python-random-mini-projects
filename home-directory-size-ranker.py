# home-directory-size-ranker.py
# Description: Scans the user's home directory to identify and rank files larger than a specified threshold and folders
# whose total size exceeds another threshold. Outputs a list of these files and folders with their sizes in megabytes.

import os
from pathlib import Path

# Define the home directory path and size thresholds for files and folders
home_path = Path.home()
threshold_file_mb = 100  # File size threshold in megabytes
threshold_folder_mb = 100  # Folder size threshold in megabytes

print('RANKING OF FILES:')
# Walk through the home directory to find and rank large files
for dirpath, dirnames, filenames in os.walk(home_path):
    for filename in filenames:
        file_path = os.path.join(dirpath, filename)
        try:
            file_size_bytes = os.path.getsize(file_path)
        except OSError:
            continue  # Skip files that cause an error

        file_size_megabytes = file_size_bytes / (1024 * 1024)
        if file_size_megabytes > threshold_file_mb:
            print(f'''
            File: {filename}
            Path: {file_path}
            Size: {file_size_megabytes:.2f} MB''')

print('\nRANKING OF FOLDERS:')
# Walk through the home directory again to find and rank large folders
for dirpath, dirnames, filenames in os.walk(home_path):
    total_size_bytes = sum(os.path.getsize(os.path.join(dirpath, file)) for file in filenames if
                           os.path.isfile(os.path.join(dirpath, file)))

    total_size_megabytes = total_size_bytes / (1024 * 1024)
    if total_size_megabytes > threshold_folder_mb:
        print(f'''
        Folder: {dirpath}
        Size: {total_size_megabytes:.2f} MB''')
