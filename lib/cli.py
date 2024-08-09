# lib/cli.py

from helpers import (
    exit_program,
    create_new_author,
    delete_author
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

        else:
            print("Invalid choice")


def menu():
    print("Please select an option:")
    print("0. Exit the program")
    print("1. See all authors")
    print("2. Create New Author")
    print("3. Delete Author")

def author_display():
    authors = Author.get_all()
    for i, author in enumerate(authors, start=1):
        print(f"{i}. {author.name}")
    print("___________________________________")
    print("Please type the # of the author to display their written works")
    print("___________________________________")
    print("0. Back to the main menu")
    print("___________________________________")
    choice = input(f"Enter the #: ")
    if choice == (f"{i}"):
        Book.find_by_author_id()
    elif choice == "0":
        menu()
    else:
        print("Invalid choice. Please try again")







if __name__ == "__main__":
    main()
