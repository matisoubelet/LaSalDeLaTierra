import mysql.connector

class Database:
    def __init__(self):
        self.db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database="LaSalDeLaTierra"
        )

    def cursor(self):
        return self.db.cursor(dictionary=True)  
    
    def commit(self):
        self.db.commit()

    def close(self):
        self.db.close()