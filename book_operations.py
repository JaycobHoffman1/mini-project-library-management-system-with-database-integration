from error_handler import ErrorHandler as e
from mysql_connector import MySQLConnector as c
from user_operations import UserOperations as u
from datetime import date as d, timedelta as t

class BookOperations:
    def __init__(self):
        self.__error_handler = e()
        self.__isbn_pattern = r"^\d{3}-\d{4}-\d{4}-\d-\d$"
        self.__publication_date_pattern = r"^\d{4}-\d{2}-\d{2}$"
        self.__user_operations = u()

    def get_error_handling(self):
        return self.__error_handler
    
    def get_isbn_pattern(self):
        return self.__isbn_pattern
    
    def get_publication_date_pattern(self):
        return self.__publication_date_pattern
    
    def get_user_operations(self):
        return self.__user_operations
    
    def set_e(self, new_e):
        self.__error_handler = new_e

    def set_isbn_pattern(self, new_isbn_pattern):
        self.__isbn_pattern = new_isbn_pattern

    def set_publication_date_pattern(self, new_publication_date_pattern):
        self.__publication_date_pattern = new_publication_date_pattern

    def set_user_operations(self, new_user_operations):
        self.__user_operations = new_user_operations

    def check_if_authors(self, cursor, conn): # Checks if authors are present in "library_management_system_db"
        query = "SELECT * FROM authors;"

        try:
            cursor.execute(query)
        except Exception as e:
            print(f"Error: {e}.")
        else:
            if cursor.fetchall():
                return True
            
            print("\nPlease add an author before adding a book.")

            cursor.close()
            conn.close()

            return False
        
    def check_if_books(self, cursor, conn): # Check if books are present in "library_management_system_db"
        query = "SELECT * FROM books;"

        try:
            cursor.execute(query)
        except Exception as e:
            print(f"Error: {e}.")
        else:
            if cursor.fetchall():
                return True
            
            print("\nPlease add a book before borrowing/returning one.")

            cursor.close()
            conn.close()

            return False
        
    def check_if_users(self, cursor, conn): # Checks if users are present in "library_management_system_db"
        query = "SELECT * FROM users;"

        try:
            cursor.execute(query)
        except Exception as e:
            print(f"Error: {e}.")
        else:
            if cursor.fetchall():
                return True
            
            print("\nPlease add a user before borrowing a book.")

            cursor.close()
            conn.close()

            return False 

    def get_author_name(self, book, cursor): # Gets "name" from "authors" table according to "id"
        author_id = (book[1],)
        author_query = """
        SELECT name FROM authors
        WHERE id = %s;
        """
        try:
            cursor.execute(author_query, author_id)
        except Exception as e:
            print(f"Error: {e}.")

            return

        return cursor.fetchall()[0][0]
    
    def get_id(self, cursor, query, identifier, id_type): # Gets "id" from specified table according to table's other "UNIQUE" column
        try:
            cursor.execute(query, (identifier,))

            _id = cursor.fetchall()[0][0]
        except Exception as e:
            print(f"\n{id_type} not found.")

            return False
        else:
            return _id
        
    def change_availability(self, conn, cursor, availability_query, book_id, str): # Changes books availability status
        try:
            cursor.execute(availability_query, (book_id,))
            conn.commit()

            print(f"\nBook {str}!")
        except Exception as e:
            print(f"\nError: {e}.")

            return False

    def add_new_book(self): # Adds book to "library_management_system_db"
        conn = c.connect_database()
        cursor = conn.cursor()

        # Checks is authors are present

        if not self.check_if_authors(cursor, conn):
            return
        
        print("\nAdd new book:\n")

        title = self.get_error_handling().validate_input_length("Enter book title: ", 255, "Title")
        author_id = self.get_error_handling().validate_integer("Enter author ID: ", "Author ID")
        isbn = self.get_error_handling().validate_input("Enter book ISBN (XXX-XXXX-XXXX-X-X): ", self.get_isbn_pattern(), "ISBN")
        publication_date = self.get_error_handling().validate_input("Enter book publication date (yyyy-mm-dd): ", self.get_publication_date_pattern(), "publication date")
        conn = c.connect_database()
        cursor = conn.cursor()
        new_book = (title, author_id, isbn, publication_date)
        query = """
        INSERT INTO books (title, author_id, isbn, publication_date)
        VALUES
        (%s, %s, %s, %s);
        """

        try:
            cursor.execute(query, new_book)
            conn.commit()
        except Exception as e:
            print(f"\nError: {e}.")
        else:
            print("\nBook added!")

        cursor.close()
        conn.close()

    def borrow_book(self): # Inserts specified book into "borrowed_books" table and changes it's availability status
        conn = c.connect_database()
        cursor = conn.cursor()

        # Checks if books and users are present

        if not self.check_if_books(cursor, conn):
            return
        
        if not self.check_if_users(cursor, conn):
            return

        print("\nBorrow a book:\n")

        # SQL operations in separate function to ensure "conn" and "cursor" are still closed if Exception is raised
        def perform_sql_operations():
            library_id = self.get_error_handling().validate_input("Enter the library ID of the user borrowing the book (ABC-1234): ",\
            self.get_user_operations().get_library_id_pattern(), "library ID")
            isbn = self.get_error_handling().validate_input("Enter the ISBN of the book you wish to borrow (XXX-XXXX-XXXX-X-X): ", self.get_isbn_pattern(), "ISBN")
            user_id_query = """
            SELECT id FROM users
            WHERE library_id = %s;
            """
            book_id_query = """
            SELECT id FROM books
            WHERE isbn = %s;
            """
            availability_query = """
            UPDATE books
            SET availability = 0
            WHERE id = %s;
            """
            user_id = self.get_id(cursor, user_id_query, library_id, "User")

            if not user_id:
                return

            book_id = self.get_id(cursor, book_id_query, isbn, "Book")
            
            if not book_id:
                return

            borrowed_book = (user_id, book_id, d.today(), d.today() + t(days = 21))
            insert_borrowed_book_query = """
            INSERT INTO borrowed_books (user_id, book_id, borrow_date, return_date)
            VALUES (%s, %s, %s, %s);
            """
            try:
                cursor.execute(insert_borrowed_book_query, borrowed_book)
                conn.commit()
            except Exception as e:
                print(f"\nError: {e}.")

                return

            if not self.change_availability(conn, cursor, availability_query, book_id, "borrowed"):
                return
            
        perform_sql_operations()
        cursor.close()
        conn.close()

    def return_book(self): # Similar structure to "borrow_book()"
        conn = c.connect_database()
        cursor = conn.cursor()

        if not self.check_if_books(cursor, conn):
            return
        
        if not self.check_if_users(cursor, conn):
            return
        
        print("\nReturn a book:\n")

        def perform_sql_operations():
            library_id = self.get_error_handling().validate_input("Enter the library ID of the user returning the book (ABC-1234): ",\
            self.get_user_operations().get_library_id_pattern(), "library ID")
            isbn = self.get_error_handling().validate_input("Enter the ISBN of the book you wish to return (XXX-XXXX-XXXX-X-X): ", self.get_isbn_pattern(), "ISBN")
            book_id_query = """
            SELECT id FROM books
            WHERE isbn = %s;
            """
            user_id_query = """
            SELECT id FROM users
            WHERE library_id = %s;
            """
            availability_query = """
            UPDATE books
            SET availability = 1
            WHERE id = %s;
            """
            user_id = self.get_id(cursor, user_id_query, library_id, "User")

            if not user_id:
                return
            
            book_id = self.get_id(cursor, book_id_query, isbn, "Book")

            if not book_id:
                return

            returned_book = (user_id, book_id)
            delete_returned_book_query = """
            DELETE FROM borrowed_books
            WHERE user_id = %s AND book_id = %s;
            """
            try:
                cursor.execute(delete_returned_book_query, returned_book)
                conn.commit()
            except Exception as e:
                print(f"Error: {e}.")

                return

            if not self.change_availability(conn, cursor, availability_query, book_id, "returned"):
                return
            
        perform_sql_operations()
        cursor.close()
        conn.close()

    def search_for_book(self): # Allows user to search for and display book details
        print("\nSearch for a book:\n")

        conn = c.connect_database()
        cursor = conn.cursor()
        isbn = (self.get_error_handling().validate_input("Enter the ISBN of the book you wish to search for (XXX-XXXX-XXXX-X-X): ", self.get_isbn_pattern(), "ISBN"),)
        query = """
        SELECT * FROM books
        WHERE isbn = %s;
        """

        try:
            cursor.execute(query, isbn)
        except Exception as e:
            print(f"Error: {e}.\n")
        else:
            details = cursor.fetchall()

            if details:
                book = details[0][1:]
                author_name = self.get_author_name(book, cursor)

                print(f"\nBook found!\n\n\
Title: {book[0]}\n\
Author: {author_name}\n\
ISBN: {book[2]}\n\
Publication Date: {book[3]}\n\
Availability: {'Available' if book[4] else 'Borrowed'}")
            else:
                print("\nBook not found.")

        cursor.close()
        conn.close()

    def display_all_books(self): # Lists all books in "library_management_db" in formatted manner
        print("\nDisplay all books:")

        conn = c.connect_database()
        cursor = conn.cursor()
        query = "SELECT * FROM books;"

        try:
            cursor.execute(query)
        except Exception as e:
            print(f"\nError: {e}.")
        else:
            details = cursor.fetchall()

            if details:
                for row in details:
                    book = row[1:]
                    author_name = self.get_author_name(book, cursor)

                    print(f"\nTitle: {book[0]}\n\
Author: {author_name}\n\
ISBN: {book[2]}\n\
Publication Date: {book[3]}\n\
Availability: {'Available' if book[4] else 'Borrowed'}")
            else:
                print("\nNo books to display.")

        cursor.close()
        conn.close()