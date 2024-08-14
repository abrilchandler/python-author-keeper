# README.md

## This project is meant to be a personal book library for the user. They can view genres, titles, and author of each book. The user will also be able to view all the authors and their birth year.

## Installation

 Fork and clone this repo to your loacal environment

'''pipenv install'''

followed by 

'''pipenv shell''' 

to install and access the necessary dependencies. 

To run the CLI database, run 

'''python lib/cli.py'''

then follow the prompts to access all parts of the database!

If you are kicked out of the CLI database at any time, rerun 

'''python lib/cli.py'''

## Helpers file
My display_books_for_author method allows the user to input the number of the authors listed to see a list of the books in the database that were written by that author. 

My delete_book and delete_author allow for the deleting of the selected instance. Both call class methods get_all() from their perspective classes, delete_book from Book and delete_author from Author. Then based on the user's choice, the chosen object will be deleted.

My create_new_author and create_new_book allow for the adding of objects. They allow the user to input the attribue values which have validating logic within their attribute setter methods.

My search_author and search_book are fairly similar to the update_author and update_book. First they have te user input the name of the book or author they wish to search for or update. The search methods print the corresponding the instance that was inputted. While the updated methods will use the same find_by_name methods provided by the Author and Book classes, the updated methos will then ask for the new values that the user wishes to replace.

## CLI file
This file lays out the menus that will be shown to the user along with print messages they will see as they navigate their way through the CLI application. the book_display and author_display methods both utilize a for loop to iterate through a list they retrieve using a get_all method prior in order to enumerate (or assign numbers) to each of the items within the list.

The menu starts out with options to "See all authors", "See all books", "Search for 

## models.author & models.book files
Within these files I initialize the values of the attributes for book objects in the class Book and author objects in the class Author. The __init__ method is repsonsible for setting the initial values. Next, I use the @property decorator to use getter methods for each attribute. Then, the @attribute.setter decorators are used to set the new values of the attribute and have some additional validation logic.



