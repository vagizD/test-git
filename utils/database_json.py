"""
Same data storage but using JSON instead of CSV.

JSON file format:

[
    {
        'name': 'Clean Code',
        'author': 'Robert',
        'read': '0'
    }
]

"""

import json

books_file = 'books_json.json'


def get_books():
    with open(books_file, 'r') as file:
        books = json.load(file)  # returns a Python dictionary
        return books


def _save_all_books(books):
    with open(books_file, 'w') as outfile:
        json.dump(books, outfile, indent=4)


def add_book(name, author):
    books = get_books()
    books.append({'name': name, 'author': author, 'read': False})
    print(f"{name} by {author} is added successfully.")
    _save_all_books(books)


def delete_book(name):
    books = get_books()
    for i in range(len(books)):
        if books[i]['name'] == name:
            books.remove(books[i])
            print(f"{name} is removed successfully.")
    _save_all_books(books)


def mark_a_book_as_read(name):
    books = get_books()
    for i in range(len(books)):
        if books[i]['name'] == name:
            books[i]['read'] = True
            print(f"{name} read status is changed to read successfully.")
    _save_all_books(books)
