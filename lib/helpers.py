# lib/helpers.py
from models.author import Author
from models.book import Book


def select_author_by_number(authors):
    choice = int(input("Enter the number of the author you want to see the books of: "))
    #authors = Author.get_all()
    if choice - 1 < len(authors) and authors[choice - 1]:
        author = authors[choice - 1]
        books = author.books_by_author()
        print("______________________________")
        print(f"Books written by {author.name}({author.birth_year}): ")
        for i, book in enumerate(books, start = 1):
            print(f"{i}. {book.name}, {book.genre}")
            print("____________________________")

        create_book_choice = input("Do you want to add a book? (y/n) or would you like to delete or update a book? (d/u): ")
        if create_book_choice.lower() == "y":
            create_new_book(author)
        elif create_book_choice.lower() == "d":
            delete_book(author)
        elif create_book_choice.lower() == "u":
            update_book(author)
    else:
        print(f"No books found for {choice}")


def create_new_author():
    name = input("Enter the author's name: ")
    birth_year = int(input("Enter the author's birth year: "))
    author = Author.create(name, birth_year)
    print("Author created successfully")
    print("____________________________")
    

def delete_author():
    choice = int(input("Enter the number of the author you want to delete: "))
    authors = Author.get_all()
    if choice - 1 < len(authors) and authors[choice - 1]:
        author = authors[choice - 1]
        author.delete()
        print("Author deleted successfully")
        print("____________________________")
    else:
        print("Author not found")

def create_new_book(author):
    name = input("Enter the book's name: ")
    genre = input("Enter the book's genre: ")
    book = Book.create(name, genre, author.id)
    print("Book created successfully")
    print("____________________________")


def delete_book(author):
    books = author.books_by_author()
    if len(books) > 0:
        print("______________________________")
        print(f"Books written by {author.name}({author.birth_year}): ")
        for i, book in enumerate(books, start=1):
            print(f"{i}. {book.name}, {book.genre}")
        print("____________________________")

        choice = int(input("Enter the number of the book you want to delete: "))
        if choice -1 < len(books):
            books = books[choice - 1]
            book.delete()
            print("Book deleted successfully!")
        else:
            print("Invalid choice.")
    else:
        print(f"No books found for {author.name}({author.birth_year}).")



def update_author():
    choice = int(input("Enter the number of the author you want to update: "))
    authors = Author.get_all()
    if choice - 1 < len(authors) and authors[choice - 1]:
        author = authors[choice - 1]
        new_name = input("Enter the new name for the author: ")
        new_birth_year = int(input("Enter the new birth year for the author: "))

        author.name = new_name
        author.birth_year = new_birth_year
        author.update()
        print("Author updated successfully")
        print("____________________________")
    else:
        print("Author not found")

def update_book(author):
    books = author.books_by_author()

    if len(books) > 0:
        print("______________________________")
        print(f"Books written by {author.name}({author.birth_year}): ")
        for i, book in enumerate(books, start=1):
            print(f"{i}. {book.name}, {book.genre}")
        print("____________________________")
        choice = int(input("Enter the number of the book you want to update: "))
        if choice - 1 < len(books):
            book = books[choice - 1]
            new_name = input("Enter the new name of the book: ")
            new_genre = input("Enter the new genre of the book: ")
            book.name = new_name
            book.genre = new_genre
            book.update()
            print("Book updated successfully")
            print("____________________________")
        else:
            print("Book not found")
    else:
        print(f"No book found for {author.name}.")

def exit_program():
    print("Goodbye!")
    exit()

