"""
Concerned with storing and retrieving books from a csv file.

csv format (interesting thing is that we use CSV file format but do not use any of CSV module methods):

name,author,read/n
name,author,read/n
name,author,read/n

As first, I was thinking about the retrieval of data from the file at the very beginning, and the storage of changes
before quiting. But then Jose said about the usage of file in every method. Moreover, the app.py deals with menu,
it does not communicate to the file with data directly, whereas all the changes to file with data are made in the
database.py.

"""

import csv

# books = [] == we no longer need it so we change it to:
books_file = 'books_csv.txt'


def add_book(name, author):
    with open(books_file, 'a') as file:  # append mode goes to the last character which means we need to
        # add a backslash n at the end of every row
        file.write(f"{name},{author},0\n")

    print(f"{name} by {author} is added to collection successfully.")


# Not a good idea to define the delete method like this, since elements are disappearing while the iteration goes on.
# def delete_book(name):
#     for book in books:
#         if book['name'] == name:
#             books.remove(book)
#             print(f"{name} is successfully removed from your collection.")
#             break
#     else:
#         print("Ops, there is no such a book in your collection!")

# a better way is to use list comprehensions with condition:


def delete_book(name):
    books = get_books()
    new_books = [book for book in books if book['name'] != name]
    _save_all_books(new_books)


def mark_a_book_as_read(name):
    books = get_books()
    for line in books:
        if line['name'] == name:
            line['read'] = '1'
    _save_all_books(books)  # private function for convention
    # _save_all_books() method has underscore in front of it which tells other developers to not call this function
    # since it modifies the content of the file. It is used for convenience only inside this file.


def _save_all_books(books):  # gets a list of lists
    with open(books_file, 'w') as file:
        for book in books:
            file.write(f"{book['name']},{book['author']},{book['read']}\n")
            # this one makes our file look as it was initially with all the changes made. Notice that if we use
            # file.write(book) we would get the same result but in a slightly different format:
            # [name,author,read]
            # [name,author,read] etc.


def get_books():
    try:
        with open(books_file, 'r') as file:
            lines = [line.strip().split(',') for line in file.readlines()]
    except FileNotFoundError:
        return []
    else:
        # so the read lines() method returns the list of elements.
        # Format (without .split(): [name,author,read,name,author,read,name,author,read])
        # With the strip() method we get rid of unnecessary characters.
        # .split(',') helps us to make a list of lists from that file data because it splits all initial elements (which
        # were lines with name,author,read)
        # now we need to construct our book dictionaries with another list comprehensions:
        return [
            {'name': line[0], 'author': line[1], 'read': line[2]}
            for line in lines
        ]