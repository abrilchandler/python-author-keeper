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

def display_author_for_book():
    pass

def book_display():
    books = Book.get_all()
    for i, book in enumerate(books, start=1):
        print(f"{i}. {book.name}")
    print("___________________________________")
    print("D. Display the author of a book")
    print("___________________________________")
    print("B. Back to the main menu")
    print("___________________________________")
    choice = input("Enter your choice: ")

    if choice == "B":
        main()
    elif choice == "D":
        name = input("Enter the name of the book: ")
        book = Book.find_by_name(name)
        if book:
            display_author_for_book()


def exit_program():
    print("Goodbye!")
    exit()
