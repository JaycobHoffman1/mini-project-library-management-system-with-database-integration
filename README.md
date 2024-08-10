# Mini-Project: Library Management System with Database Integration

- Author: Jaycob Hoffman

- Date: 9 August 2024

## Documentation

The Library Management System with Database Integration is a CLI application that allows the user to create and manage data on books, authors, and library ID holders on the "library_management_system_db" MySQL database.

### Main Features

- **Book Operations**: With the ```Book operations``` feature, the user can add books, borrow books, return books, search for a specific book, and display all books on the "library_management_system_db" MySQL database.
- **User Operations**: With the ```User operations``` feature, the user can add library ID holders under unique library IDs, search for a specific library ID holder, and display all library ID holders on the "library_management_system_db" MySQL database.
- **Author Operations**: With the ```Author operations``` feature, the user can add authors, search for a specific author, and display all authors on the "library_management_system_db" MySQL database.

### Bonus Features

- **Duplicate Detection**: When adding an instance of a book or user, the program will detect and notify the user when a duplicate identifier (ISBN or library ID) is added.

### UI

When the user first runs the Library Management System with Database Integration, the following UI will display:

```
Welcome to the Library Management System with Database Integration!
****

Main Menu:
1. Book Operations
2. User Operations
3. Author Operations
4. Quit

Please select an option from the menu above:
```

The user can select an option from the menu by entering the number that precedes it. Each selection (except for "Quit") will take the user to a separate menu, where they can then select a task. This cycle will continue indefinitely until the user selects option #4 and quits the program. Then, the following message will display:

```
Quitting program. Thank you for using the Library Management System with Database Integration!
```

The menus are as follows:

Book operations:
```
Book Operations:
1. Add a new book
2. Borrow a book
3. Return a book
4. Search for a book
5. Display all books
6. Main menu
```

User operations:
```
User Operations:
1. Add a new user
2. View user details
3. Display all users
4. Main menu
```

Author operations:
```
Author Operations:
1. Add a new author
2. View author details
3. Display all authors
4. Main menu
```

When the task has finished, the menu will display again and prompt the user to select another option. This cycle will continue indefinitely until the user selects the "Main menu" option, in which they will be returned to the main menu.

### Errors

The Library Management System with Database Integration will raise errors with accompanying messages under the following circumstances:

- ```ValueError```: If any input is blank or consists entirely of spaces.
- ```ValueError```: If a regex pattern does not match an indicated input, where applicable.
- ```ValueError```: If the user enters a non-numeric value when making a menu selection.
- ```ValueError```: If the user enters an input that exceeds the specified character limit.
- ```ValueError```: If the user enters a non-integer value when prompted to enter an integer.
- ```NotInRangeError```: If the user enters a numeric value that does not appear on the menu when making a menu selection.
- Additionally, the Library Management System with Database Integration will raise a variety of ```Exception```s, all printed in a formatted manner, when a SQL query fails to execute as intended. Examples of such failures may include, but are not limited to, searching for a library ID or ISBN that does not exist when borrowing a book, failure to connect a cursor, and attempting to add a duplicate book or library user.

#

View the Library Management System with Database Integration [GitHub Repository](https://github.com/JaycobHoffman1/mini-project-library-management-system-with-database-integration)