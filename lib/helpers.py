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

def exit_program():
    print("Goodbye!")
    exit()
