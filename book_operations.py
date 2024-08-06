from error_handler import ErrorHandler as e

class BookOperations:
    def __init__(self):
        self.__error_handler = e()
        self.__isbn_pattern = r"^\d{3}-\d{4}-\d{4}-\d-\d$"

    def get_e(self):
        return self.__error_handler
    
    def get_isbn_pattern(self):
        return self.__isbn_pattern
    
    def set_e(self, new_e):
        self.__error_handler = new_e

    def set_isbn_pattern(self, new_isbn_pattern):
        self.__isbn_pattern = new_isbn_pattern

    def add_new_book(self):
        title = self.get_e().validate_input_length("Enter the book title: ", 255, "Title")
        author_id = self.get_e().validate_integer("Enter author ID: ", "Author ID")
        isbn = self.get_e().validate_input("Enter book ISBN: ", self.get_isbn_pattern(), "ISBN")
        ###