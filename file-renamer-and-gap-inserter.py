# file-renamer-and-gap-inserter.py
# Description: Organizes files in a specified directory by either renaming them to maintain a sequential numbering
# or by inserting gaps in the numbering. Useful for managing files like 'spam001.txt', ensuring consistent naming or making space for new files.

import os
import re


def extract_number(filename):
    """Extracts the numeric part from filenames formatted as 'spamXXX'."""
    pattern = re.compile(r'spam(\d{3})')
    match = re.search(pattern, filename)
    return int(match.group(1)) if match else None


def sort_files(files_list):
    """Sorts a list of filenames based on their numeric part."""
    return sorted(files_list, key=extract_number)


def rename_files(folder_path):
    """Renames files in the specified folder to maintain sequential numbering without gaps."""
    matching_files = [f for f in os.listdir(folder_path) if re.match(r'spam\d{3}', f)]
    sorted_files = sort_files(matching_files)

    for i, filename in enumerate(sorted_files, start=1):
        new_filename = f'spam{i:03d}.txt'
        os.rename(os.path.join(folder_path, filename), os.path.join(folder_path, new_filename))
        print(f'Renamed {filename} to {new_filename}')


def insert_gap(folder_path, start_index, gap_size):
    """Inserts a gap in the numbering of files starting from the specified index."""
    matching_files = sort_files([f for f in os.listdir(folder_path) if re.match(r'spam\d{3}', f)])

    for filename in reversed(matching_files):
        file_number = extract_number(filename)
        if file_number >= start_index:
            new_filename = f'spam{file_number + gap_size:03d}.txt'
            os.rename(os.path.join(folder_path, filename), os.path.join(folder_path, new_filename))
            print(f'Moved {filename} to {new_filename}')


def main():
    """Main function to handle user input for renaming files or inserting gaps."""
    print('''
    Choose an option:
    1. Rename files to fill the name gap.
    2. Insert gaps in numbered files for new files.
    ''')

    choice = input("Enter your choice (1 or 2): ")
    directory = ""  # Replace with your actual folder path

    if choice == '1':
        rename_files(directory)
    elif choice == '2':
        start_index = int(input("Enter the starting index for the gap: "))
        gap_size = int(input("Enter the size of the gap: "))
        insert_gap(directory, start_index, gap_size)
    else:
        print("Invalid choice.")


if __name__ == "__main__":
    main()
