from error_handler import ErrorHandler as e

class UserInterface:
    def __init__(self):
        self.__error_handler = e()
        self.__prompt = "Please select an option from the menu above: "

    def get_e(self):
        return self.__error_handler
    
    def get_prompt(self):
        return self.__prompt
    
    def set_e(self, new_e):
        self.__error_handler = new_e

    def set_prompt(self, new_prompt):
        self.__prompt = new_prompt

    def display_user_interface(self):
        def display_book_operations():
            while True:
                print("Book Operations:\n\
1. Add a new book\n\
2. Borrow a book\n\
3. Return a book\n\
4. Search for a book\n\
5. Display all books\n\
6. Main menu")
            
                user_input = self.get_e().check_if_in_range(self.get_prompt(), 6)

                if user_input == 1:
                    pass
                elif user_input == 2:
                    pass
                elif user_input == 3:
                    pass
                elif user_input == 4:
                    pass
                elif user_input == 5:
                    pass
                elif user_input == 6:
                    break

        def display_user_operations():
            while True:
                print("User Operations:\n\
1. Add a new user\n\
2. View user details\n\
3. Display all users\n\
4. Main menu")
                
                user_input = self.get_e().check_if_in_range(self.get_prompt(), 4)

                if user_input == 1:
                    pass
                elif user_input == 2:
                    pass
                elif user_input == 3:
                    pass
                elif user_input == 4:
                    break

        def display_author_operations():
            while True:
                print("Author Operations:\n\
1. Add a new author\n\
2. View author details\n\
3. Display all authors\n\
4. Main menu")
                
                user_input = self.get_e().check_if_in_range(self.get_prompt(), 4)

                if user_input == 1:
                    pass
                elif user_input == 2:
                    pass
                elif user_input == 3:
                    pass
                elif user_input == 4:
                    break

        print("Welcome to the Library Management System with Database Integration!\n****")
        
        while True:
            print("Main Menu:\n\
1. Book Operations\n\
2. User Operations\n\
3. Author Operations\n\
4. Quit")
            
            user_input = self.get_e().check_if_in_range(self.get_prompt(), 4)

            if user_input == 1:
                display_book_operations()
            elif user_input == 2:
                display_user_operations()
            elif user_input == 3:
                display_author_operations()
            elif user_input == 4:
                print("Quitting program. Thank you for using the Library Management System with Database Integration!")

                break

user_interface = UserInterface()

user_interface.display_user_interface()