from error_handler import ErrorHandler as e
from book_operations import BookOperations as b
from author_operations import AuthorOperations as a
from user_operations import UserOperations as u

class UserInterface:
    def __init__(self):
        self.__error_handler = e()
        self.__prompt = "Please select an option from the menu above: "
        self.__book_operations = b()
        self.__author_operations = a()
        self.__user_operations = u()

    def get_error_handling(self):
        return self.__error_handler
    
    def get_prompt(self):
        return self.__prompt
    
    def get_book_operations(self):
        return self.__book_operations
    
    def get_author_operations(self):
        return self.__author_operations
    
    def get_user_operations(self):
        return self.__user_operations
    
    def set_e(self, new_e):
        self.__error_handler = new_e

    def set_prompt(self, new_prompt):
        self.__prompt = new_prompt

    def set_book_operations(self, new_book_operations):
        self.__book_operations = new_book_operations

    def set_author_operations(self, new_author_operations):
        self.__author_operations = new_author_operations

    def set_user_operations(self, new_user_operations):
        self.__user_operations = new_user_operations

    def display_user_interface(self): # Main user interface
        def display_book_operations(): # Book operations menu
            while True:
                print("\nBook Operations:\n\
1. Add a new book\n\
2. Borrow a book\n\
3. Return a book\n\
4. Search for a book\n\
5. Display all books\n\
6. Main menu\n")
            
                user_input = self.get_error_handling().check_if_in_range(self.get_prompt(), 6)

                if user_input == 1:
                    self.get_book_operations().add_new_book()
                elif user_input == 2:
                    self.get_book_operations().borrow_book()
                elif user_input == 3:
                    self.get_book_operations().return_book()
                elif user_input == 4:
                    self.get_book_operations().search_for_book()
                elif user_input == 5:
                    self.get_book_operations().display_all_books()
                elif user_input == 6:
                    break

        def display_user_operations(): # User operations menu
            while True:
                print("\nUser Operations:\n\
1. Add a new user\n\
2. View user details\n\
3. Display all users\n\
4. Main menu\n")
                
                user_input = self.get_error_handling().check_if_in_range(self.get_prompt(), 4)

                if user_input == 1:
                    self.get_user_operations().add_new_user()
                elif user_input == 2:
                    self.get_user_operations().view_user_details()
                elif user_input == 3:
                    self.get_user_operations().display_all_users()
                elif user_input == 4:
                    break

        def display_author_operations(): # Author operations menu
            while True:
                print("\nAuthor Operations:\n\
1. Add a new author\n\
2. View author details\n\
3. Display all authors\n\
4. Main menu\n")
                
                user_input = self.get_error_handling().check_if_in_range(self.get_prompt(), 4)

                if user_input == 1:
                    self.get_author_operations().add_new_author()
                elif user_input == 2:
                    self.get_author_operations().view_author_details()
                elif user_input == 3:
                    self.get_author_operations().display_all_authors()
                elif user_input == 4:
                    break

        print("\nWelcome to the Library Management System with Database Integration!\n****")
        
        while True:
            print("\nMain Menu:\n\
1. Book Operations\n\
2. User Operations\n\
3. Author Operations\n\
4. Quit\n")
            
            user_input = self.get_error_handling().check_if_in_range(self.get_prompt(), 4)

            if user_input == 1:
                display_book_operations()
            elif user_input == 2:
                display_user_operations()
            elif user_input == 3:
                display_author_operations()
            elif user_input == 4:
                print("\nQuitting program. Thank you for using the Library Management System with Database Integration!\n")

                break