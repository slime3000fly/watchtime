# https://www.psycopg.org/docs/usage.html
import psycopg2

class DatabaseHandler():

    def __init__ (self, database = "exampledb", user = "docker", passoword = "password", host = "localhost"):
        self.database = database
        self.user = user
        self.password = password
        self.host = host
        self.conn = None

    def connect(self):
        # Connect to existing database
        self.conn = psycopg2.connect(
            database="exampledb",
            user="docker",
            password="docker",
            host="localhost"
        )

    def close_connections(self):
        if self.conn is not None:
            self.conn.close()


    def createUser(self,username,password):
        # Open cursor to perform database operation
        cur = self.conn.cursor()

        # temporary date
        username = "slime3000fly"
        password = "n"

        # Selct queery to check if username exist
        cur.execute("SELECT * FROM login WHERE username = %s", (username,))
        existing_record = cur.fetchone()

        # if username dosen't exist, create new record 
        if existing_record is None:
            cur.execute("INSERT INTO login (username, password) VALUES (%s, %s)", (username, password))
            self.conn.commit()
            print("User created sucesfully")
        else:
            print("User allready exist")

        cur.close()