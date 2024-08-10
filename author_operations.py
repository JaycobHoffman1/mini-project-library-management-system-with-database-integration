from error_handler import ErrorHandler as e
from mysql_connector import MySQLConnector as c

class AuthorOperations:
    def __init__(self):
        self.__error_handler = e()
    
    def get_error_handling(self):
        return self.__error_handler
    
    def set_e(self, new_error_handler):
        self.__error_handler = new_error_handler

    def add_new_author(self): # Adds author to "library_management_system_db"
        print("\nAdd new author:\n")

        name = self.get_error_handling().validate_input_length("Enter author name: ", 255, "Author name")
        biography = self.get_error_handling().check_input("Enter author biography: ", "Biography")
        conn = c.connect_database()
        cursor = conn.cursor()
        new_author = (name, biography)
        query = """
        INSERT INTO authors (name, biography)
        VALUES
        (%s, %s);
        """

        try:
            cursor.execute(query, new_author)
            conn.commit()
        except Exception as e:
            print(f"\nError: {e}.")
        else:
            print("\nAuthor added!")

        cursor.close()
        conn.close()
    
    def view_author_details(self): # Allows user to search for and display author details
        print("\nView author details:\n")

        conn = c.connect_database()
        cursor = conn.cursor()
        name = (self.get_error_handling().check_input("Enter the name of the author you wish to search for: ", "Author name"),)
        query = """
        SELECT * FROM authors
        WHERE name = %s;
        """

        try:
            cursor.execute(query, name)
        except Exception as e:
            print(f"Error: {e}.\n")
        else:
            details = cursor.fetchall()

            if details:
                author = details[0]

                print(f"\nAuthor found!\n\n\
Author ID: {author[0]}\n\
Name: {author[1]}\n\
Biography: {author[2]}")
            else:
                print("\nAuthor not found.")

        cursor.close()
        conn.close()

    def display_all_authors(self): # Lists all authors in "library_management_system_db" in formatted manner
        print("\nDisplay all authors:")

        conn = c.connect_database()
        cursor = conn.cursor()
        query = "SELECT * FROM authors;"

        try:
            cursor.execute(query)
        except Exception as e:
            print(f"Error: {e}.")
        else:
            details = cursor.fetchall()

            if details:
                for author in details:
                    print(f"\nAuthor ID: {author[0]}\n\
Name: {author[1]}\n\
Biography: {author[2]}")
            else:
                print("\nNo authors to display.")

        cursor.close()
        conn.close()