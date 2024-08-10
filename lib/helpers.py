# lib/helpers.py
from models.author import Author
from models.book import Book




    
def create_new_author():
    name = input("Enter the author's name: ")
    birth_year = int(input("Enter the author's birth year: "))
    author = Author.create(name, birth_year)
    print("Author created successfully")

def delete_author():
    name = input("Enter the name of the author you want to delete: ")
    author = Author.find_by_name(name)
    if author:
        author.delete()
        print("Author deleted successfully")
    else:
        print("Author not found")

def create_new_book():
    name = input("Enter the book's name: ")
    genre = input("Enter the book's genre: ")
    author_name = input("Enter the author's name: ")
    book = Book.create(name, genre, author_name)
    print("Book created successfully")

def delete_book():
    name = input("Enter the name of the book you want to delete: ")
    book = Book.find_by_name(name)
    if book:
        book.delete()
        print("Book deleted successfully")
    else:
        print("Book not found")

def display_books_for_author():
    pass

def update_author():
    name = input("Enter the name of the author you want to update: ")
    author = Author.find_by_name(name)
    if author:
        new_name = input("Enter the new name for the author: ")
        new_birth_year = int(input("Enter the new birth year for the author: "))

        author.name = new_name
        author.birth_year = new_birth_year
        author.update()
        print("Author updated successfully")
    else:
        print("Author not found")

def update_book():
    name = input("Enter the name of the book you want to update: ")
    book = book.update()

def exit_program():
    print("Goodbye!")
    exit()
