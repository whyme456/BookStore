import csv
import sqlite3

# Open the CSV file and create a reader object
with open('random_testing/Book_list.csv', 'r') as csv_file:
    reader = csv.reader(csv_file)

    # Connect to the SQLite database
    conn = sqlite3.connect('random_testing/db.sqlite3')
    cursor = conn.cursor()

    # Check if the tables already exist in the database
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='Books_genre'")
    genre_table = cursor.fetchone()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='Books_book'")
    books_table = cursor.fetchone()

    # If the tables don't exist, create them
    if not genre_table:
        cursor.execute('CREATE TABLE "Books_genre" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "name" varchar(255) NOT NULL)')
    if not books_table:
        cursor.execute('CREATE TABLE "Books_book" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "title" varchar(255) NOT NULL, "author" varchar(255) NOT NULL, "location" varchar(2) NOT NULL, "genre_id" bigint NOT NULL REFERENCES "Books_genre" ("id") DEFERRABLE INITIALLY DEFERRED, "date_created" datetime NOT NULL)')

    # Skip the first row
    next(reader)

    # Loop through each row in the CSV file
    for row in reader:
        # Check if the genre already exists in the genre table
        cursor.execute('SELECT id FROM "Books_genre" WHERE name=?', (row[3],))
        genre_id = cursor.fetchone()

        # If the genre doesn't exist, insert it into the genre table
        if not genre_id:
            cursor.execute('INSERT INTO "Books_genre" (name) VALUES (?)', (row[3],))
            genre_id = cursor.lastrowid
        else:
            genre_id = genre_id[0]

        # Set the location to "unknown" if it's empty
        location = row[4] if row[4] else "unknown"

        # Insert the book into the books table
        cursor.execute('INSERT INTO "Books_book" (title, author, genre_id, location, date_created) VALUES (?, ?, ?, ?, DATETIME("now"))', (row[1], row[2], genre_id, location))

    # Commit the changes to the database
    conn.commit()

    # Close the database connection
    conn.close()
