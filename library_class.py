# Import as needed
from mysql.connector import Error
from database_connection import connect_database
from datetime import date, timedelta
from book_class import Book # set avail, set borrow, set reserve
from user_class import User # all

# Code for class: Library

class Library:
    def add_book(self, book: object): # Method to add a new book
        conn = connect_database() # Establishing connection to database
        if conn is not None: # Verifying connection
            try:
                cursor = conn.cursor() # Activating cursor
                book_to_add = (book.get_title(), book.get_author_id(), book.get_isbn(), book.get_publish_date()) # Creating variable with book details for query
                query = "INSERT INTO books (title, author_id, isbn, publication_date) VALUES (%s, %s, %s, %s)" # Defining query to add a new book to the books table
                cursor.execute(query, book_to_add) # Execute query
                conn.commit() # Commit changes to database
                print(f"{book.get_title()} has been added to the library database.") # Updating user
            except Exception as ge: # General exception handling
                print(f"General Error Occurred: {ge}")
            except Error as dbe: # Database error handling
                print(f"Database Error Occurred: {dbe}")
            finally: # Closing cursor and connection
                cursor.close()
                conn.close()

    def borrow_book(self, book_id, user_id): # Method to borrow a book
        conn = connect_database() # Establishing database connection
        if conn is not None: # Verifying connection
            try:
                cursor = conn.cursor() # Activating cursor
                availability = False # Creating variable to update book availability status
                borrow_date = date.today() # Creating the book's borrowed date
                return_date = borrow_date + timedelta(days=7) # Creating a return date for the book
                borrowed_book = (user_id, book_id, borrow_date, return_date, availability, book_id) # Creating a variable to use the values in the query
                query = """
                    INSERT INTO borrowed_books (user_id, book_id, borrow_date, return_date) VALUES (%s, %s, %s, %s);
                    UPDATE books SET availability = %s WHERE id = %s;
                """
                cursor.execute(query, borrowed_book) # Executing query 
                conn.commit() # Committing changes to the database
                print(f"Book ID '{book_id}' has been borrowed by '{user_id}'.") # Updating user
            except Exception as ge: # General exception handling
                print(f"General Error Occurred: {ge}")
            except Error as dbe: # Database error handling
                print(f"Database Error Occurred: {dbe}")
            finally: # Closing cursor and connection
                cursor.close()
                conn.close()

    def return_book(self, book_id, user_id): # Method to return a book
        conn = connect_database() # Establishing database connection
        if conn is not None: # Verifying connection
            try:
                cursor = conn.cursor() # Activating cursor
                availability = True # Creating variable to update book's availability status
                returned_book = (user_id, book_id) # Creating a variable to use the values in the query
                availability = (availability, book_id)
                query1 = "DELETE FROM borrowed_books WHERE user_id = %s AND book_id = %s;"
                query2 = "UPDATE books SET availability = %s WHERE id = %s;"  
                cursor.execute(query1, returned_book) # Executing query 1
                cursor.execute(query2, availability) # Execute query 2
                conn.commit() # Committing changes to the database
                print(f"Book ID '{book_id}' has been returned by '{user_id}'.") # Updating user
            except Exception as ge: # General exception handling
                print(f"General Error Occurred: {ge}")
            except Error as dbe: # Database error handling
                print(f"Database Error Occurred: {dbe}")
            finally: # Closing cursor and connection
                cursor.close()
                conn.close()

    def view_books(self): # Method to print a list of book titles
        conn = connect_database() # Establish connection to the database
        if conn is not None: # Verify connection
            try:
                cursor = conn.cursor() # Activate cursor
                query = "SELECT * FROM books" # Defining the query to get all books from the books table
                cursor.execute(query) # Execute query
                for book in cursor.fetchall(): # Fetching books data from database to display
                    print(book) # Displaying data to user
            except Exception as ge: # General exception handling
                print(f"General Error Occurred: {ge}")
            except Error as dbe: # Database error handling
                print(f"Database Error Occurred: {dbe}")
            finally: # Closing cursor and connection
                cursor.close()
                conn.close()

    def search_book(self, book_id):
        conn = connect_database() # Establish connection to the database
        if conn is not None: # Verify connection
            try:
                cursor = conn.cursor() # Activate cursor
                search_book = (book_id,)
                query = "SELECT * FROM books WHERE id = %s" # Defining the query to search for the book of choice
                cursor.execute(query, search_book) # Execute query
                for book in cursor.fetchall(): # Fetching data from database to display
                    print(book) # Displaying data to user
            except Exception as ge: # General exception handling
                print(f"General Error Occurred: {ge}")
            except Error as dbe: # Database error handling
                print(f"Database Error Occurred: {dbe}")
            finally: # Closing cursor and connection
                cursor.close()
                conn.close()

    def add_author(self, author: object): # Method to add a new author
        conn = connect_database() # Establish connection to the database
        if conn is not None: # Verify connection
            try:
                cursor = conn.cursor() # Activate cursor
                author_to_add = (author.get_author_name(), author.get_author_biography()) # Creating variable with author details for query
                query = "INSERT INTO authors (name, biography) VALUES (%s, %s)" # Defining the query to add a new author to the authors table
                cursor.execute(query, author_to_add) # Execute query
                conn.commit() # Commit changes to database
                print(f"New author: {author.get_author_name()} was successfully added to the library database.") # Updating user
            except Exception as ge: # General exception handling
                print(f"General Error Occurred: {ge}")
            except Error as dbe: # Database error handling
                print(f"Database Error Occurred: {dbe}")
            finally: # Closing cursor and connection
                cursor.close()
                conn.close()

    def view_authors(self): # Method to view a list of all authors
        conn = connect_database() # Establish connection to the database
        if conn is not None: # Verify connection
            try:
                cursor = conn.cursor() # Activate cursor
                query = "SELECT * FROM authors" # Defining the query to get all authors from the authors table
                cursor.execute(query) # Execute query
                for author in cursor.fetchall(): # Fetching authors data from database to display
                    print(author) # Displaying data to user
            except Exception as ge: # General exception handling
                print(f"General Error Occurred: {ge}")
            except Error as dbe: # Database error handling
                print(f"Database Error Occurred: {dbe}")
            finally: # Closing cursor and connection
                cursor.close()
                conn.close()

    def search_author(self, author_id):
        conn = connect_database() # Establish connection to the database
        if conn is not None: # Verify connection
            try:
                cursor = conn.cursor() # Activate cursor
                search_author = (author_id,)
                query = "SELECT * FROM authors WHERE id = %s" # Defining the query to search for the author of choice
                cursor.execute(query, search_author) # Execute query
                for author in cursor.fetchall(): # Fetching data from database to display
                    print(author) # Displaying data to user
            except Exception as ge: # General exception handling
                print(f"General Error Occurred: {ge}")
            except Error as dbe: # Database error handling
                print(f"Database Error Occurred: {dbe}")
            finally: # Closing cursor and connection
                cursor.close()
                conn.close()

    def add_user(self, user: object): # Method to add a new user
        conn = connect_database() # Establish connection to the database
        if conn is not None: # Verify connection
            try:
                cursor = conn.cursor() # Activate cursor
                user_to_add = (user.get_user_name(), user.get_user_id())
                query = "INSERT INTO users (name, library_id) VALUES (%s, %s)" # Defining the query to add a new user to the users table
                cursor.execute(query, user_to_add) # Execute query
                conn.commit() # Commit changes to database
                print(f"New user: {user.get_user_name()} was successfully added to the library database.") # Updating user
            except Exception as ge: # General exception handling
                print(f"General Error Occurred: {ge}")
            except Error as dbe: # Database error handling
                print(f"Database Error Occurred: {dbe}")
            finally: # Closing cursor and connection
                cursor.close()
                conn.close()

    def view_users(self): # Method to view a list of all authors
        conn = connect_database() # Establish connection to the database
        if conn is not None: # Verify connection
            try:
                cursor = conn.cursor() # Activate cursor
                query = "SELECT * FROM users" # Defining the query to get all users from the users tables
                cursor.execute(query) # Execute query
                for user in cursor.fetchall(): # Fetching users data to display
                    print(user) # Displaying date to user
            except Exception as ge: # General exception handling
                print(f"General Error Occurred: {ge}")
            except Error as dbe: # Database error handling
                print(f"Database Error Occurred: {dbe}")
            finally: # Closing cursor and connection
                cursor.close()
                conn.close()

    def search_user(self, user_id):
        conn = connect_database() # Establish connection to the database
        if conn is not None: # Verify connection
            try:
                cursor = conn.cursor() # Activate cursor
                search_user = (user_id,)
                query = "SELECT * FROM users WHERE id = %s"
                cursor.execute(query, search_user) # Execute query 
                for user in cursor.fetchall():
                    print(user)
            # except Exception as ge: # General exception handling
            #     print(f"General Error Occurred: {ge}")
            # except Error as dbe: # Database error handling
            #     print(f"Database Error Occurred: {dbe}")
            finally: # Closing cursor and connection
                cursor.close()
                conn.close()