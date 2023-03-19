import mysql.connector
import os


class Database:
    def __init__(self, host="localhost", user="root", password=os.getenv('MYSQL_PASS'), database="school"):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.name = "students"

        # Queries
        self.display_query = f"SELECT * FROM {self.name}"
        self.add_query = f"INSERT INTO {self.name} (name, course, mobile) VALUES (%s,%s,%s)"
        self.search_query = f"SELECT * FROM {self.name} WHERE name = %s"
        self.update_query = f"UPDATE {self.name} SET name = %s, course = %s, mobile = %s WHERE id = %s"
        self.delete_query = f"DELETE FROM {self.name} WHERE id = %s"

    def connect(self):
        return mysql.connector.connect(host=self.host,
                                       user=self.user,
                                       password=self.password,
                                       database=self.database)
