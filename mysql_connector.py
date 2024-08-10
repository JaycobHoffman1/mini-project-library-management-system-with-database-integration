import mysql.connector
from mysql.connector import Error

class MySQLConnector:
    def connect_database(): # Connects to "library_management_system_db"
        try:
            conn = mysql.connector.connect(
                database = "library_management_system_db", 
                user = "root",
                password = "Jajoconi@1",
                host = "localhost"
            )
        except Error as e:
            print(f"Error: {e}")

            return False
        else:
            return conn