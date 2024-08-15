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

        create_book_choice = input("Do you want to add a book? (y/n): ")
        if create_book_choice.lower() == "y":
            create_new_book(author)
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
    # name = input("Enter the name of the author you want to delete: ")
    # author = Author.find_by_name(name)
    #if author:
        author.delete()
        print("Author deleted successfully")
        print("____________________________")
    else:
        print("Author not found")

def create_new_book(author):
    name = input("Enter the book's name: ")
    genre = input("Enter the book's genre: ")
    book = Book.create(name, genre, author.id)
    #book = Book.create(name, genre, author.name, author.id)
    print("Book created successfully")
    print("____________________________")


def delete_book():
    #name = input("Enter the name of the book you want to delete: ")
    #book = Book.find_by_name(name)
    choice = int(input("Enter the number of the book you want to delete: "))
    books = Book.find_by_author_id()
    if choice - 1 < len(books) and books[choice - 1]:
        book = books[choice - 1]
        book.delete()
        print("Book deleted successfully")
        print("____________________________")
    else:
        print("Book not found")


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

# def update_book():
#     choice = int(input("Enter the number of the book you want to update: "))
#     books = Book.get_all()
#     if choice - 1 < len(books) and books[choice - 1]:
#         book = books[choice - 1]
#         new_name = input("Enter the new name of the book: ")
#         new_genre = input("Enter the new genre of the book: ")

#         book.name = new_name
#         book.genre = new_genre
#         book.update()
#         print("Book updated successfully")
#         print("____________________________")
#     else:
#         print("Book not found")

def exit_program():
    print("Goodbye!")
    exit()



# def search_author():
#     name = input("Enter the name of the author: ")
#     author = Author.find_by_name(name)
#     if author:
#         print(f"{author.name} was born in {author.birth_year}")
#         print("____________________________")
#     else:
#         raise ValueError("Author not found")



 #   def search_book():
#     name = input("Enter the name of the book: ")
#     book = Book.find_by_name(name)
#     if book:
#         print(f"{book.name} was written by {book.author_name} and is a {book.genre} book.")
#         print("____________________________")
#     else:
#         raise ValueError("Book not found")