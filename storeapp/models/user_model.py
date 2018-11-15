'''imports for the required packages'''
from storeapp.database.dbconnector import DatabaseConnection
import psycopg2
import psycopg2.extras as dictionary
from storeapp import app


dbcon = DatabaseConnection()

class Attendant():

    def __init__(self, attendant_name, contact, password, role):
        '''Declaring all the parameters'''
        self.attendant_name = attendant_name
        self.contact = contact
        self.password = password
        self.role = role
    

    def add_attendant(self):
        '''adds a new user to the database'''
        query = """INSERT INTO attendants(attendant_name, contact, password, role) 
                    VALUES (%s, %s, %s, %s)"""      
        dbcon.cursor.execute(query, (self.attendant_name, self.contact, self.password, self.role))
        return  "You have successfully added {}".format(self.attendant_name)
