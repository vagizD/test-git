"""
Hello!
This script is universal for every of three database scripts. You just change code a little (is in comments) and the
word database_... itself.
"""

# from utils import database_json
from utils import database_sqlite3

USER_CHOICE = """
Enter:
 - 'a' to add a new book
 - 'l' to list all books
 - 'r' to mark a book as read
 - 'd' to delete a book
 - 'q' to quit

 Your choice: """


def menu():
    database_sqlite3.create_book_table()
    user_input = input(USER_CHOICE)
    if user_input == 'a':
        new_book()
    elif user_input == 'l':
        list_books()
    elif user_input == 'r':
        read()
    elif user_input == 'd':
        delete()
    elif user_input == 'q':
        exit()
    else:
        print('Unknown command. Please try again.')
    menu()


def new_book():
    new_book_name = input('Write the book name: ')
    new_book_author = input('Write the book author: ')
    database_sqlite3.add_book(new_book_name.title(), new_book_author.title())

# this one is for the csv format:
# def list_books():
#     books = database.get_books()
#     if len(books) == 0:
#         print('No books in collection yet!')
#     for book in books:
#         if book['read'] == '1':
#             print(f"{book['name']} by {book['author']}, read.")
#         else:
#             print(f"{book['name']} by {book['author']}, not read.")


def list_books():  # this one is for database_json.json file and suits the database variation as well
    books = database_sqlite3.get_books()
    if len(books) == 0:
        print("Your collection is empty for now.")
    else:
        for i in range(len(books)):
            name = books[i]['name']
            author = books[i]['author']
            if books[i]['read']:
                print(f"{name}, by {author}, read")
            else:
                print(f"{name}, by {author}, not read yet")


def read():
    read_book_name = input('Write the book name: ')
    database_sqlite3.mark_a_book_as_read(read_book_name.title())


def delete():
    deleted_book_name = input('Write the book name: ')
    database_sqlite3.delete_book(deleted_book_name.title())


menu()
