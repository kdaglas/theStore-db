'''package imports '''
from storeapp.database.dbconnector import DatabaseConnection
from storeapp.models.user_model import Attendant
import psycopg2
import psycopg2.extras as dictionary


dbcon = DatabaseConnection()

class UserDatabaseQueries():

    '''performing certain queries to the database'''

    def authenticate_attendant(self, attendant_name, password):
        '''logging in a user'''
        query = """SELECT attendant_name, password FROM attendants WHERE attendant_name = %s and password = %s"""
        dbcon.cursor.execute(query, (attendant_name, password,))
        login = dbcon.cursor.fetchone()
        return login


    def fetch_all_attendants(self):
        '''retieves all the attendants'''
        query = """SELECT * FROM attendants"""
        dbcon.cursor.execute(query)
        attendants = dbcon.cursor.fetchall()
        return attendants


    def fetch_one_attendant(self, attendantId):
        '''gets one attendant'''
        query = """SELECT * FROM attendants WHERE attendantId = %s"""
        dbcon.cursor.execute(query, (attendantId,))
        attendant = dbcon.cursor.fetchone()
        return attendant


    def get_attendant_by_name(self, attendant_name):
        '''return an attendant by name'''
        query = """SELECT * FROM attendants WHERE attendant_name = %s"""
        dbcon.cursor.execute(query, (attendant_name,))
        attendant = dbcon.cursor.fetchone()
        return attendant


    def get_attendant_by_contact(self, contact):
        '''checks if attendant contact already exists'''
        query = """SELECT * FROM attendants WHERE contact = %s"""
        dbcon.cursor.execute(query, (contact,))
        attendant = dbcon.cursor.fetchone()
        return attendant


    def get_attendant_by_role(self, role):
        '''bring back an attendant by role'''
        query = """SELECT * FROM attendants WHERE role = %s"""
        dbcon.cursor.execute(query, (role,))
        attendant = dbcon.cursor.fetchone()
        return attendant


    def promote_to_admin(self, role, attendantId):
        '''updating role of a user'''
        query = """UPDATE attendants SET role = %s WHERE attendantId = %s"""
        dbcon.cursor.execute(query, (attendantId, role,))
        promoted = dbcon.cursor.rowcount
        return promoted


    def delete_user(self, attendantId):
        '''deletes attendant from the database'''
        query = """DELETE FROM attendants WHERE attendantId = %s"""
        dbcon.cursor.execute(query, (attendantId,))
        deleted_attendant = dbcon.cursor.rowcount
        return deleted_attendant
