# excel-album-categorizer-by-decade-genre.py
# Description: Reads music album data from an Excel spreadsheet, categorizes albums by their release decade and genre,
# and prints a summary of albums organized by these categories. This helps in analyzing music trends over time.

import openpyxl

def get_decade(year):
    """
    Converts a year into the start year of its decade (e.g., 1994 becomes 1990).
    """
    return (year // 10) * 10

# Load the workbook and access the specified sheet
file = "path/to/your/music_albums.xlsx"  # Replace with the path to your spreadsheet
workbook = openpyxl.load_workbook(file)
sheet = workbook.active  # Assumes the data is in the active sheet

# Dictionary to hold album information categorized by decade and genre
albums_by_decade_genre = {}

# Process each row in the sheet to extract album information
for row in sheet.iter_rows(min_row=2, values_only=True):
    try:
        # Normalize and extract album data
        album = {
            'title': row[0],
            'artist': row[1],
            'year': int(row[2]),
            'genre': row[3].strip().lower()
        }
    except ValueError as e:
        print(f"Error processing row {row}: {e}")
        continue  # Skip rows with invalid data

    decade = get_decade(album['year'])  # Determine the album's decade

    # Initialize nested dictionaries for new decades and genres
    albums_by_decade_genre.setdefault(decade, {}).setdefault(album['genre'], []).append(album)

# Print a summary of albums organized by decade and genre
for decade, genres in sorted(albums_by_decade_genre.items()):
    print(f"Decade: {decade}s")
    for genre, albums in sorted(genres.items()):
        print(f" Genre: {genre.title()}, Number of Albums: {len(albums)}")
        for album in albums:
            print(f"   {album['title']} by {album['artist']} ({album['year']})")
