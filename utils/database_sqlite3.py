"""
Using the sqlite3 to store the data.
Going to the next level!

We will try to have the same list of dictionaries format within the intermediary steps.
"""

import sqlite3

books_database = 'books_data.db'


def create_book_table():
    connection = sqlite3.connect(books_database)
    cursor = connection.cursor()

    cursor.execute('CREATE TABLE IF NOT EXISTS books (name text primary key, author text, read integer)')
# id is not used since we have only one table in our database. We will not relate it to any other.
    connection.commit()
    connection.close()


def get_books():
    connection = sqlite3.connect(books_database)
    cursor = connection.cursor()

    cursor.execute('SELECT * FROM books')
    # books = cursor.fetchall()  # gives a list of tuples: [(name, author, read), (name, author, read)]
    # since we want to have dictionaries instead of tuples and save the initial format for our program:
    books = [{'name': row[0], 'author': row[1], 'read': row[2]} for row in cursor.fetchall()]
    # we end uop with a list of dictionaries

    # here, we do not need any connection.commit() since we do not have anything to save to the disk.
    # connection.commit()
    connection.close()

    return books


def add_book(name, author):
    books = get_books()
    for book in books:
        if book['name'] == name:
            print(f"Sorry, but this book already exists in your database!")
            break
    else:
        connection = sqlite3.connect(books_database)
        cursor = connection.cursor()

        cursor.execute('INSERT INTO books VALUES (?, ?, 0)', (name, author))
        # make sure that you created a tuple
        connection.commit()
        connection.close()


def delete_book(name):
    connection = sqlite3.connect(books_database)
    cursor = connection.cursor()

    cursor.execute('DELETE FROM books WHERE name = ?', (name,))  # comma is necessary to make a tuple

    connection.commit()
    connection.close()


def mark_a_book_as_read(name):
    connection = sqlite3.connect(books_database)
    cursor = connection.cursor()

    cursor.execute('UPDATE books SET read = 1 WHERE name = ?', (name,))  # comma is necessary to make a tuple

    connection.commit()
    connection.close()
