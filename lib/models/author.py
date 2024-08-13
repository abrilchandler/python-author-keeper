from . import CURSOR, CONN

class Author:

    all = {}

    def __init__(self, name, birth_year, id = None):
        self.name = name
        self.birth_year = birth_year
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

    @property
    def birth_year(self):
        return self._birth_year
    
    
    @birth_year.setter
    def birth_year(self, birth_year):
        if isinstance(birth_year, int):
            self._birth_year = birth_year
        else:
            raise ValueError("Birth year must be an integer")
        
    @classmethod
    def create_table(cls):
        """ Create a new table to persist the attributes of Department instances """
        sql = """
            CREATE TABLE IF NOT EXISTS authors (
            id INTEGER PRIMARY KEY,
            name TEXT,
            birth_year INTEGER)
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        """ Drop the table that persists Department instances """
        sql = """
            DROP TABLE IF EXISTS authors;
        """
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        """ Insert a new row with the name and birth_year values of the current Author instance.
        Update object id attribute using the primary key value of new row.
        Save the object in local dictionary using table row's PK as dictionary key"""
        sql = """
            INSERT INTO authors (name, birth_year)
            VALUES (?, ?)
        """

        CURSOR.execute(sql, (self.name, self.birth_year))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    @classmethod
    def create(cls, name, birth_year):
        """ Initialize a new Author instance and save the object to the database """
        author = cls(name, birth_year)
        author.save()
        return author
    
    def update(self):
        """Update the table row corresponding to the current Author instance."""
        sql = """
            UPDATE authors
            SET name = ?, birth_year = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.name, self.birth_year, self.id))
        CONN.commit()

    def delete(self):
        """Delete the table row corresponding to the current Author instance,
        delete the dictionary entry, and reassign id attribute"""

        sql = """
            DELETE FROM authors
            WHERE id = ?
        """

        CURSOR.execute(sql, (self.id,))
        CONN.commit()

        # Delete the dictionary entry using id as the key
        del type(self).all[self.id]

        # Set the id to None
        self.id = None

    def add_book(self, book):
        """ Adda book associated with the current author"""
        book.author_id = self.id
        book.save()


    @classmethod
    def instance_from_db(cls, row):
        """Return a Author object having the attribute values from the table row."""

        # Check the dictionary for an existing instance using the row's primary key
        author = cls.all.get(row[0])
        if author:
            # ensure attributes match row values in case local instance was modified
            author.name = row[1]
            author.location = row[2]
        else:
            # not in dictionary, create new instance and add to dictionary
            author = cls(row[1], row[2])
            author.id = row[0]
            cls.all[author.id] = author
        return author

    @classmethod
    def get_all(cls):
        """Return a list containing a Author object per row in the table"""
        sql = """
            SELECT *
            FROM authors
        """

        rows = CURSOR.execute(sql).fetchall()

        return [cls.instance_from_db(row) for row in rows]

    @classmethod
    def find_by_id(cls, id):
        """Return a Author object corresponding to the table row matching the specified primary key"""
        sql = """
            SELECT *
            FROM authors
            WHERE id = ?
        """

        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None

    @classmethod
    def find_by_name(cls, name):
        """Return a Author object corresponding to first table row matching specified name"""
        sql = """
            SELECT *
            FROM authors
            WHERE name is ?
        """

        row = CURSOR.execute(sql, (name,)).fetchone()
        return cls.instance_from_db(row) if row else None

#instance method because it is retrieving books associated with the current author instance
    def books_by_author(self):
        """Return list of books associated with current author"""
        from .book import Book
        sql = """
            SELECT * FROM books
            WHERE author_id = ?
        """
        CURSOR.execute(sql, (self.id,),)

        rows = CURSOR.fetchall()
        return [
            Book.instance_from_db(row) for row in rows
        ]
