from . import CURSOR, CONN
from models.author import Author


class Book:

    all = {}

# automatically called when you create a new instance (object) of a class.
#_init__ method is to initialize the attributesvariables) of the class, 
# it means that this method is responsible for setting the 
# initial values of the object's attributes.
    def __init__(self, name, genre, author_name, id = None):
        self.name = name
        self.genre = genre
        self.author_name = author_name
        self.id = id

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name):
            self._name = name
        else:
            raise ValueError("Name must be a string")

    #responsible for getting the value of the attribute
    @property
    def genre(self):
        return self._genre
    
    #sets value of the given attribute, can include validation logic
    @genre.setter
    def genre(self, genre):
        if isinstance(genre, str) and len(genre):
            self._genre = genre
        else:
            raise ValueError("Genre must be a string")
        
    @property
    def author_id(self):
        return self._author_name
    
    @author_id.setter
    def author_id(self, author_name):
        if isinstance is str and Author.find_by_name(author_name):
            self._author_name = author_name
        else:
            raise ValueError("author_name must reference a department in the database")
        

    @classmethod
    def create_table(cls):
        """ Create a new table to persist the attributes of Book instances """
        sql = """
            CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY,
            name TEXT,
            genre TEXT,
            author_name INTEGER,
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        """ Drop the table that persists Book instances """
        sql = """
            DROP TABLE IF EXISTS books;
        """
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        """ Insert a new row with the name, genre, and author id values of the current Book object.
        Update object id attribute using the primary key value of new row.
        Save the object in local dictionary using table row's PK as dictionary key"""
        sql = """
                INSERT INTO books (name, genre, author_name)
                VALUES (?, ?, ?)
        """

        CURSOR.execute(sql, (self.name, self.genre, self.author_name))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    
    def update(self):
        """Update the table row corresponding to the current Book instance."""
        sql = """
            UPDATE books
            SET name = ?, genre = ?, author_name = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.name, self.genre,
                             self.author_name, self.id))
        CONN.commit()

    def delete(self):
        """Delete the table row corresponding to the current Book instance,
        delete the dictionary entry, and reassign id attribute"""

        sql = """
            DELETE FROM books
            WHERE id = ?
        """

        CURSOR.execute(sql, (self.id,))
        CONN.commit()

        # Delete the dictionary entry using id as the key
        del type(self).all[self.id]

        # Set the id to None
        self.id = None

    @classmethod
    def create(cls, name, genre, author_name):
        """ Initialize a new Book instance and save the object to the database """
        book = cls(name, genre, author_name)
        book.save()
        return book

    @classmethod
    def instance_from_db(cls, row):
        """Return an Book object having the attribute values from the table row."""

        # Check the dictionary for  existing instance using the row's primary key
        book = cls.all.get(row[0])
        if book:
            # ensure attributes match row values in case local instance was modified
            book.name = row[1]
            book.genre = row[2]
            book.author_name = row[3]
        else:
            # not in dictionary, create new instance and add to dictionary
            book = cls(row[1], row[2], row[3])
            book.id = row[0]
            cls.all[book.id] = book
        return book
    
    @classmethod
    def get_all(cls):
        """Return a list containing one Book object per table row"""
        sql = """
            SELECT *
            FROM books
        """

        rows = CURSOR.execute(sql).fetchall()

        return [cls.instance_from_db(row) for row in rows]

    @classmethod
    def find_by_id(cls, id):
        """Return Book object corresponding to the table row matching the specified primary key"""
        sql = """
            SELECT *
            FROM books
            WHERE id = ?
        """

        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None
    
    @classmethod
    def find_by_name(cls, name):
        """Return Employee object corresponding to first table row matching specified name"""
        sql = """
            SELECT *
            FROM books
            WHERE name is ?
        """

        row = CURSOR.execute(sql, (name,)).fetchone()
        return cls.instance_from_db(row) if row else None
    
    @classmethod
    def find_by_author_name(cls, author_name):
        sql = """
            SELECT *
            FROM books
            WHERE author_name = ?
        """
        rows = CURSOR.execute(sql, (author_name,)).fetchall()
        return cls.instance_from_db(rows) if rows else None 
