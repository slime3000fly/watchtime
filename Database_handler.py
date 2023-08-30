# https://www.psycopg.org/docs/usage.html
import psycopg2

class DatabaseHandler():

    """
    A class for handling database operations using psycopg2 library.
    """

    def __init__ (self, database = "watchtime", user = "docker", password = "docker", host = "localhost"):
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
        
        print("_connect method called")
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

    def __check_item_existence(self,item,table,where):
        """
        Checks if a user with the given username exists in the database.

        Args:
            username (str): The username to check.

        Returns:
            bool: True if the user exists, False otherwise.
        """

        self._connect()
        cur = self.conn.cursor() # Open cursor to perform database operation
        query = f"SELECT * FROM {table} WHERE {where} = %s"
        cur.execute(query, (item,))
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

        if not self.__check_item_existence(username,'login','username'):
            self._connect()
            cur = self.conn.cursor()
            cur.execute("INSERT INTO login (username, password) VALUES (%s, %s)", (username, password))
            self.conn.commit() # add record to table
            cur.close()
            self._close_connection()
            print("User created successfully.")
        else:
            print("User already exists.")     

    def delete_item(self,item,table,where):
        """
        Deletes a record from the database table based on a specific condition.

        Args:
            item (str): The value of the item to be deleted.
            table (str): The name of the table from which the item should be deleted.
            where (str): The column name representing the condition for deletion.

        The function checks if a record with the specified value exists in the specified table,
        based on the provided condition. If a matching record is found, it is deleted from the table.

        Args:
            item (str): The value of the item to be deleted.
            table (str): The name of the table from which the item should be deleted.
            where (str): The column name representing the condition for deletion.

        Note:
            This function assumes a valid database connection has been established using `_connect`.
            The condition provided in the `where` argument should be a valid SQL WHERE clause.
        """
       
        if self.__check_item_existence(item,table,where):
            self._connect()
            cur = self.conn.cursor()
            query = f"DELETE FROM {table} WHERE {where} = %s"
            cur.execute(query, (item,))
            self.conn.commit()  # delete record from table
            cur.close()
            self._close_connection()
            print("User deleted successfully.")
        else:
            print("User does not exist.")

    def create_app (self,app):
        """
        Creates a new app in the 'appdata' table if it doesn't exist.

        Args:
            app (str): The name of the app.

        Note:
            This function checks whether the app already exists in the 'appdata' table
            using the `__check_item_existence` method. If the app doesn't exist, a new
            record is added to the table.
        """

        if not self.__check_item_existence(app,'appdata','app_name'):
            self._connect()
            cur = self.conn.cursor()
            cur.execute("INSERT INTO appdata (app_name) VALUES (%s)", (app,))
            self.conn.commit() # add record to table
            cur.close()
            self._close_connection()

    def create_date (self,user_id,date):
        """
        Creates a new date record in the 'watchtimedata' table.

        Args:
            user_id (int): The ID of the user.
            date (str): The date in the format 'YYYY-MM-DD'.

        Note:
            This function checks if the provided user_id exists in the 'login' table
            using the `__check_item_existence` method. If the user_id is valid, a new
            record with the user_id and date is added to the 'watchtimedata' table.
        """
        
        if self.__check_item_existence(user_id,'login','id'):
            self._connect()
            cur = self.conn.cursor()
            cur.execute("INSERT INTO watchtimedata (user_id,data_date) VALUES (%s, %s)", (user_id,date,))
            self.conn.commit() # add record to table
            cur.close()
            self._close_connection()

    def get_all_users(self):
        """
        Retrieves all users from the login table.

        Returns:
            list: A list of dictionaries representing the user records.
        """
        self._connect()
        cur = self.conn.cursor()
        query = "SELECT * FROM login"
        query = f"SELECT * FROM login WHERE id = %s"
        cur.execute(query,(35,))
        users = cur.fetchall()
        cur.close()
        self._close_connection()
        return users
    
    def create_apptime(self,data_id,app_id,time_spent):
        """
        Creates a new record in the 'apptime' table.

        Args:
            data_id (int): The ID of the user data.
            app_id (int): The ID of the app.
            time_spent (int): The time spent on the app.

        Note:
            This function assumes valid data_id and app_id values exist in the respective tables.
        """
        if self.__check_item_existence(data_id,'watchtimedata','data_id'):
            if self.__check_item_existence(app_id,'appdata','app_id'):
                self._connect()
                cur = self.conn.cursor()
                cur.execute("INSERT INTO apptime (data_id,app_id,time_spent) VALUES (%s, %s, %s)", (data_id,app_id,time_spent))
                self.conn.commit() # add record to table
                cur.close()
                self._close_connection()





