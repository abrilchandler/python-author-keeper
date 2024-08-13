# lib/cli.py

from helpers import (
    exit_program,
    create_new_author,
    delete_author,
    create_new_book,
    delete_book,
    search_author,
    search_book,
    update_author,
    update_book,
    display_books_for_author
)
from models.author import Author
from models.book import Book


def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            author_display()
        elif choice == "2":
            book_display()
        elif choice == "3":
            search_author()
        elif choice == "4":
            search_book()
        else:
            print("Invalid choice")


def menu():
    print("Please select an option:")
    print("___________________________________")
    print("0. Exit the program")
    print("___________________________________")
    print("1. See all authors")
    print("___________________________________")
    print("2. See all books")
    print("___________________________________")
    print("3. Search for a author by name")
    print("___________________________________")

    

def author_display():
    authors = Author.get_all()
    for i, author in enumerate(authors, start=1):
        print(f"{i}. {author.name}")
    print("___________________________________")
    print("C. Create a new author")
    print("___________________________________")
   # print("S. Search for a author by name")
   # print("___________________________________")
    print("D. Display books by author")
    print("___________________________________")
    print("X. Delete author")
    print("___________________________________")
    print("U. Update author details")
    print("___________________________________")
    print("B. Back to the main menu")
    print("___________________________________")
    choice = input("Enter your choice: ")
   

    if choice == "B":
        main()
    elif choice == "C":
        create_new_author()
    elif choice == "U":
        update_author()
    elif choice == "X":
        delete_author()
   # elif choice == "S":
   #     search_author()
    elif choice == "D":
        display_books_for_author()
    else:
        print("Not Valid")
   

def book_display():
    books = Book.get_all()
    for i, book in enumerate(books, start=1):
        print(f"{i}. {book.name}, {book.author_name}")
    print("___________________________________")
    print("C. Create a new book")
    print("___________________________________")
    # print("S. Search for a book by name")
    # print("___________________________________")
    print("X. Delete a book")
    print("___________________________________")
    print("U. Update book details")
    print("___________________________________")
    print("B. Back to the main menu")
    print("___________________________________")
    choice = input("Enter your choice: ")


    if choice == "B":
        main()
    elif choice == "C":
        create_new_book()
    elif choice == "X":
        delete_book()
    elif choice == "U":
        update_book()
    # elif choice == "S":
    #     search_book()
    else:
        print("Not Valid")
        



if __name__ == "__main__":
        main()
