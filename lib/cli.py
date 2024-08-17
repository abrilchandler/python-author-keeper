# lib/cli.py

from helpers import (
    exit_program,
    create_new_author,
    delete_author,
    create_new_book,
    delete_book,
    update_author,
    update_book,
    select_author_by_number
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
        else:
            print("Invalid choice")


def menu():
    print("-----------------------------------")
    print("Please select an option by number:")
    print("___________________________________")
    print("0. Exit the program")
    print("___________________________________")
    print("1. See all authors")
    print("___________________________________")

    

def author_display():
    #using the Author class method to get_all of the author instances in a list
    #using enumerate to iterate through the list of authors and print them out with numbers
    authors = Author.get_all()
    for i, author in enumerate(authors, start=1):
        print(f"{i}. {author.name}")
    print("___________________________________")
    print("C. Create a new author")
    print("___________________________________")
    print("S. Select author by number")
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
        author_display()
    elif choice == "U":
        update_author()
        author_display()
    elif choice == "X":
        delete_author()
        author_display()
    elif choice == "S":
        select_author_by_number(authors)
        author_display()
    else:
        print("Not Valid")
   



if __name__ == "__main__":
        main()
