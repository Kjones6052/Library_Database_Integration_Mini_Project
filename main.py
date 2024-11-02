# Main interactive script for user interactions
# Import as needed
import re
from library_class import Library
from book_class import Book
from author_class import Author
from user_class import User


def main(): # Print intro and main menu with user input to choose action
    intro = "\nWelcome to the Library Management System with Database Integration!\n****"
    library = Library()
    while True:
        print(intro)
        user_input = input("Main Menu:\n1. Book Opertations\n2. Author Operations\n3. User Operations\n4. Close Library Management System\nPlease enter your option number (1-4): ")
        if user_input == "1": # Enter Book Operations Menu
            book_op = input("Book Operations Menu:\n1. Add a New Book\n2. Borrow a Book\n3. Return a Book\n4. Search for a Book\n5. Display All Books\n6. Close Library Management System\nPlease enter your option number (1-6): ")
            if book_op == "1": # Get details and run add book method (title, author_id, isbn, publication_date, availability)
                book_title = input("Enter the Title of the book: ") 
                book_author_id = input("Enter the ID # of the Author of the book: ")
                try:
                    if re.search(r"\d", book_author_id):
                        book_isbn = input("Enter the ISBN of the book: ")
                        if re.search(r"\d", book_isbn):
                            pub_date = input("Enter the Publishing Date of the book (using numerical yyyy-mm-dd format): ")
                            if re.search(r"\d{4}-\d{2}-\d{2}", pub_date):
                                book = Book(book_title, book_author_id, book_isbn, pub_date)
                                library.add_book(book)
                            else:
                                ValueError("Incorrect Date Format: please use numbers in the day-month-year format.")
                        else:
                           raise ValueError("Letters found in Book ISBN, no letters allowed in Book ISBN.")
                    else:
                        raise ValueError("Digits found in Author Name, no digits allowed in Author ID #.")
                except ValueError as e:
                    print(e)
            elif book_op == "2": # Get details and run borrow book method (book_id, user_id)
                book_id = input("Enter book ID #: ")
                user_id = input("Enter user ID #: ")
                found = False
                try:
                    if re.search(r"\d", book_id) and re.search(r"\d", user_id):
                        library.borrow_book(book_id, user_id)
                    else:
                        raise ValueError
                except ValueError:
                    print("Invalid entry, please use only numbers.")
            elif book_op == "3": # Get details and run return book method (book_title, user)
                found = False
                book_id = input("Enter book ID #: ")
                user_id = input("Enter user ID #: ")
                try:
                    if re.search(r"\d", book_id) and re.search(r"\d", user_id):
                        library.return_book(book_id, user_id)
                    else:
                        raise ValueError
                except ValueError:
                    print("Invalid entry, please use only numbers.")
            elif book_op == "4": # Get details and run search book method (book_id)
                found = False
                book_id = input("Enter book ID #: ")
                try:
                    if re.search(r"\d", book_id):
                        library.search_book(book_id)
                    else:
                        raise ValueError
                except ValueError:
                    print("Invalid entry, please use only numbers.")
            elif book_op == "5": # Get run display books method
                library.view_books()
            elif book_op == "6": 
                break
            else:
                print("Invalid option, please enter a digit 1-7.")
        elif user_input == "2": # Create Author Operations Menu
            author_op = input("Author Operations Menu:\n1. Add a New Author\n2. View Author Details\n3. Display All Authors\n4. Close Library Management System\nPlease enter your option number (1-4): ")
            if author_op == "1": # Get details and run add author method (name, biography)
                author_name = input("Enter Author's Name: ") 
                author_bio = input("Enter Author's Biography: ")
                if re.search(r"\d", author_name):
                    print("Error: Digits found in Author Name, please try again.")
                else:
                    author = Author(author_name, author_bio)
                    library.add_author(author)
            elif author_op == "2": # Get details and run search author method
                author_id = input("Enter Author ID #: ")
                found = False
                if re.search(r"\d", author_id):
                    found = True
                    if found == True:
                        library.search_author(author_id)
                else:
                    print("Error: Letters found in Author ID, please only enter numbers.")
            elif author_op == "3": # Get view authors method
                library.view_authors()
            elif author_op == "4": 
                break
            else:
                print("Invalid option, please enter a digit 1-4.")
        elif user_input == "3": # Create User Operations Menu
            user_op = input("User Operations Menu:\n1. Add a New User\n2. View User Details\n3. Display All Users\n4. Close Library Management System\nPlease enter your option number (1-4): ")
            if user_op == "1": # Get details and run add user method (name, library_id)
                user_name = input("Enter name: ") 
                library_id = input("Enter Library ID #: ")
                try:
                    if re.search(r"\d", user_name):
                        raise ValueError("Error: Digits found in User Name, please use only letters and spaces.")
                    else:    
                        if re.search(r"\d", library_id):
                            print(f"Adding {user_name} to the Library Management System.")
                            user = User(user_name, library_id)
                            library.add_user(user)
                        else:
                            raise ValueError("Error: Invalid Library ID Number, please use only numerical digits.")
                except Exception as e:
                    print(e)
            elif user_op == "2": # Get details and run view details method (name)
                user_id = input("Enter User ID #: ")
                found = False
                if re.search(r"\d", user_id):
                    found = True
                    if found == True:
                        library.search_user(user_id)
                else:
                    print("Error: Letters found in User ID, please only enter numbers.")
            elif user_op == "3": # Get view users method
                library.view_users()
            elif user_op == "4":
                break
            else:
                print("Invalid option, please enter a digit 1-4.")
        elif user_input == "4": 
            break
        else:
            print("Invalid option, please enter a digit 1-4.")

if __name__ == "__main__":
    main()