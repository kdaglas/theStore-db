from storeapp.database.dbconnector import DatabaseConnection
import psycopg2
import psycopg2.extras as dictionary
from storeapp import app
import datetime


dbcon = DatabaseConnection()

'''Object classes for the attendant model'''
class Attendant():

    def __init__(self, attendant_name, contact, password, role):
        '''Declaring all the parameters'''
        self.attendant_name = attendant_name
        self.contact = contact
        self.password = password
        self.role = role


    def check_same_credits(self):
        '''method to check if both usernam and password existin the db'''
        dbcon.cursor.execute("""SELECT attendant_name, password FROM attendants WHERE attendant_name = %s and password = %s""",
                            (self.attendant_name, self.password,))
        login = dbcon.cursor.fetchone()
        return login

    def get_attendant_by_name(self):
        '''method to return an attendant by name the db'''
        try:
            dbcon.cursor.execute("""SELECT * FROM attendants WHERE attendant_name = %s""",(self.attendant_name,))
            attendant = dbcon.cursor.fetchone()
            return attendant
        except:
            return "Attendant with that id doesnot exist"
            