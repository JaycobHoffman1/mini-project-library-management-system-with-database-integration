import re

"""
This module handles user errors occurring within the program.
Errors pertaining to the MySQL database "library_management_system_db" are handled within their respective class methods
"""

class NotInRangeError(Exception): # Custom error that raises when user enter number not on menu when making menu selection
    def raise_error():
        raise NotInRangeError

class ErrorHandler:
    def check_input(self, user_input, input_type): # Ensures input is not blank/comprised of only spaces
        while True:
            _input = input(user_input)

            try:
                if (not _input) or len(_input) == _input.count(" "):
                    raise ValueError(f"{input_type} cannot be blank.")
            except ValueError as v:
                print(v)
            else:
                return _input
            
    def check_if_in_range(self, user_input, max_value, input_type = "Field"): # Ensures user menu selection is within specified range
        while True:
            try:
                _input = int(self.check_input(user_input, input_type))

                if _input < 1 or _input > max_value:
                    NotInRangeError.raise_error()
            except NotInRangeError:
                print("Input not in range specified on menu.")
            except ValueError:
                print("Please enter a valid numeric value.")
            else:
                return _input
            
    def validate_input_length(self, user_input, max_value, input_type = "Field"): # Ensures user input does not exceed character limit
        while True:
            _input = self.check_input(user_input, input_type)

            try:
                if len(_input) > max_value:
                    NotInRangeError.raise_error()
            except NotInRangeError:
                print(f"Input exceeds {max_value} characters.")
            else:
                return _input
            
    def validate_integer(self, user_input, input_type = "Field"): # Ensures user input is an integer
        while True:
            try:
                _input = int(self.check_input(user_input, input_type))
            except ValueError:
                print("Please enter a valid numeric value.")
            else:
                return _input
            
    def validate_input(self, user_input, pattern, input_type): # Ensures user input matches regex pattern
        while True:
            _input = self.check_input(user_input, f"{input_type[0].upper()}{input_type[1:]}") 
            # Avoids using ".capitalize()" to preserve the case of "ISBN" when it is passed as a parameter

            try:
                if not re.search(pattern, _input):
                    raise ValueError(f"Invalid {input_type}.")
            except ValueError as v:
                print(v)
            else:
                return _input