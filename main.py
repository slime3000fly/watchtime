# https://www.psycopg.org/docs/usage.html
import psycopg2

class DatabaseHandler():

    """
    A class for handling database operations using psycopg2 library.
    """

    def __init__ (self, database = "exampledb", user = "docker", password = "password", host = "localhost"):
        """
        Initializes a DatabaseHandler object with connection parameters.

        Args:
            database (str): The name of the database.
            user (str): The username for database authentication.
            password (str): The password for database authentication.
            host (str): The host where the database is located.
        """

        self.database = database
        self.user = user
        self.password = password
        self.host = host
        self.conn = None

    def _connect(self):
        """
        Establishes a connection to the database.
        """

        self.conn = psycopg2.connect(
            database= self.database,
            user= self.user,
            password= self.password,
            host= self.host
        )

    def _close_connection(self):
        """
        Closes the connection to the database if it's open.
        """
        
        if self.conn is not None:
            self.conn.close()

    def __check_user_existence(self,username):
        """
        Checks if a user with the given username exists in the database.

        Args:
            username (str): The username to check.

        Returns:
            bool: True if the user exists, False otherwise.
        """

        self._connect()
        cur = self.conn.cursor() # Open cursor to perform database operation
        cur.execute("SELECT * FROM login WHERE username = %s", (username,))
        existing_record = cur.fetchone() # get record from previos querry
        cur.close() # close cursor
        self._close_connection()
        return existing_record is not None


    def create_user(self,username,password):
        """
        Creates a new user in the database.

        Args:
            username (str): The username of the new user.
            password (str): The password of the new user.
        """

        if not self.__check_user_existence(username):
            self._connect()
            cur = self.conn.cursor()
            cur.execute("INSERT INTO login (username, password) VALUES (%s, %s)", (username, password))
            self.conn.commit() # add record to table
            cur.close()
            self._close_connection()
            print("User created successfully.")
        else:
            print("User already exists.")     
