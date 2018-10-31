from thestoreapp.database.dbconnector import DatabaseConnection
from thestoreapp.models.user_model import Attendant
import psycopg2
import psycopg2.extras as dictionary


dbcon = DatabaseConnection()

class DatabaseQueries():

    '''these are methods to perform certain queries to the database'''
    def authenticate_attendant(self, attendant_name, password):
        '''method for logging in an attendant'''
        query = """SELECT attendant_name, password FROM attendants WHERE attendant_name = %s and password = %s"""
        dbcon.cursor.execute(query, (attendant_name, password,))
        login = dbcon.cursor.fetchone()
        return login


    def get_attendant_by_name(self, attendant_name):
        '''method to return an attendant by name the db'''
        query = """SELECT * FROM attendants WHERE attendant_name = %s"""
        dbcon.cursor.execute(query, (attendant_name,))
        attendant = dbcon.cursor.fetchone()
        return attendant


    def get_attendant_by_contact(self, contact):
        '''method that checks if attendant contact is already added in the database'''
        query = """SELECT * FROM attendants WHERE contact = %s"""
        dbcon.cursor.execute(query, (contact,))
        attendant = dbcon.cursor.fetchone()
        return attendant


    def promote_to_admin(self, role, attendantId):
        '''this method returns the new admin'''
        dbcon.cursor.execute("""UPDATE attendants SET role = %s WHERE attendantId = %s""", (attendantId, role,))
