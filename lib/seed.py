from models.__init__ import CONN, CURSOR
from models.author import Author
from models.book import Book

def reset_database():
    Book.drop_table()
    Author.drop_table()
    Author.create_table()
    Book.create_table()


reset_database()
print("Tables created!")