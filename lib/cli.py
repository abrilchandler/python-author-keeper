# lib/cli.py

from helpers import (
    exit_program,
    create_new_author,
    delete_author,
    create_new_book,
    delete_book
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
            create_new_author()
        elif choice == "3":
            delete_author()
        elif choice == "4":
            create_new_book()
        elif choice == "5":
            delete_book()
        elif choice == "6":
            book_display()
        else:
            print("Invalid choice")


def menu():
    print("Please select an option:")
    print("0. Exit the program")
    print("1. See all authors")
    print("2. Create New Author")
    print("3. Delete Author")
    print("4. Create New Book")
    print("5. Delete Book")
    print("6. See all books")

    

def author_display():
    authors = Author.get_all()
    for i, author in enumerate(authors, start=1):
        print(f"{i}. {author.name}")
    print("___________________________________")
    print("Please type the # of the author to display their written works")
    print("___________________________________")
    print("B. Back to the main menu")
    print("___________________________________")
    choice = input("Enter your choice: ")
    # number_picked = int(input("Enter the #: "))
    # if 1 <= number_picked <= len(authors):
    #     selected_author = author[number_picked - 1]
    #     print(f"You selected: {selected_author.name}")
    #     books = Book.find_by_author_id(selected_author.id)
    # if books:
    #     print(f"Books written by {selected_author.name}:")
    #     for book in books:
    #         print(book.name)
    #     else:
    #         print("No books found for the selected author.")
    if choice == "B":
        menu()
    # else:
    #     print("Invalid choice. Please try again")

def book_display():
    books = Book.get_all()
    for i, book in enumerate(books, start=1):
        print(f"{i}. {book.name}")
    print("___________________________________")
    print("Please type the # of the author to display their written works")
    print("___________________________________")
    print("B. Back to the main menu")
    print("___________________________________")
    choice = input("Enter your choice: ")

    if choice == "B":
        menu()



if __name__ == "__main__":
    main()
