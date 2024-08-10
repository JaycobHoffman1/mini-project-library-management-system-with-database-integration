from error_handler import ErrorHandler as e
from mysql_connector import MySQLConnector as c

class UserOperations:
    def __init__(self):
        self.__error_handler = e()
        self.__library_id_pattern = r"^[A-Z]{3}-\d{4}$"

    def get_error_handling(self):
        return self.__error_handler
    
    def get_library_id_pattern(self):
        return self.__library_id_pattern
    
    def set_e(self, new_e):
        self.__error_handler = new_e

    def set_library_id_pattern(self, new_library_id_pattern):
        self.__library_id_pattern = new_library_id_pattern

    def add_new_user(self): # Adds user to "library_management_system_db"
        print("\nAdd new user:\n")

        name = self.get_error_handling().validate_input_length("Enter user name: ", 255, "User name")
        library_id = self.get_error_handling().validate_input("Enter user library ID (ABC-1234): ", self.get_library_id_pattern(), "library ID")
        conn = c.connect_database()
        cursor = conn.cursor()
        new_user = (name, library_id)
        query = """
        INSERT INTO users (name, library_id)
        VALUES
        (%s, %s);
        """

        try:
            cursor.execute(query, new_user)
            conn.commit()
        except Exception as e:
            print(f"\nError: {e}.")
        else:
            print("\nUser added!")

        cursor.close()
        conn.close()
    
    def view_user_details(self): # Allows user to search for and display details according to "library_id"
        print("\nView user details:\n")

        conn = c.connect_database()
        cursor = conn.cursor()
        library_id = (self.get_error_handling().validate_input("Enter the library ID of the user you wish to search for (ABC-1234): ",\
        self.get_library_id_pattern(), "library ID"),)
        query = """
        SELECT * FROM users
        WHERE library_id = %s;
        """

        try:
            cursor.execute(query, library_id)
        except Exception as e:
            print(f"Error: {e}.\n")
        else:
            details = cursor.fetchall()

            if details:
                user = details[0][1:]

                print(f"\nUser found!\n\n\
Name: {user[0]}\n\
Library ID: {user[1]}")
            else:
                print("\nUser not found.")

        cursor.close()
        conn.close()

    def display_all_users(self): # Lists all users in "library_management_system_db" in formatted manner
        print("\nDisplay all users:")

        conn = c.connect_database()
        cursor = conn.cursor()
        query = "SELECT * FROM users;"

        try:
            cursor.execute(query)
        except Exception as e:
            print(f"Error: {e}.")
        else:
            details = cursor.fetchall()

            if details:
                for row in details:
                    user = row[1:]

                    print(f"\nName: {user[0]}\n\
Library ID: {user[1]}")
            else:
                print("\nNo users to display.")

        cursor.close()
        conn.close()