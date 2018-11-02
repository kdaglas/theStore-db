import unittest
import json
# from flask_jwt_extended import create_access_token
from storeapp import app
from storeapp.database.dbconnector import DatabaseConnection
from storeapp.models.user_model import Attendant


dbcon = DatabaseConnection()

class Testing(unittest.TestCase):

    '''checking user data'''
    registering_attendant = json.dumps(dict(attendant_name="Douglas", contact="+256-755-598090", password="Callme2"),)
    add_product = json.dumps(dict(product_name="Cookies", unit_price="800", quantity="20", category="foodish"),)

    wrong_fields = json.dumps(dict(attendant="Douglas", contact="+256-755-598090", password="Callme2"),)
    same_values = json.dumps(dict(attendant_name="Douglas", contact="+256-755-598090", password="Callme2"),)
    same_contact = json.dumps(dict(attendant_name="Douglas", contact="+256-755-598090", password="Callme2"),)

    invalid_customer = json.dumps(dict(attendant_name="Douglas", contact="+256-755-598090", password="Callme2"),)
    wrong_contact = json.dumps(dict(attendant_name="Douglas", contact="+256755598090", password="Callme2"),)
    wrong_username = json.dumps(dict(attendant_name="", contact="+256-755-598090", password="Callme2", category="necessity"),)
    wrong_password = json.dumps(dict(attendant_name="", contact="+256-755-598090", password="Callme2", category="necessity"),)


    empty_attendant_name = json.dumps(dict(attendant_name="", contact="+256-755-598090", password="Callme2"),)
    empty_contact = json.dumps(dict(attendant_name="Douglas", contact="", password="Callme2"),)
    empty_password = json.dumps(dict(attendant_name="Douglas", contact="+256-755-598090", password=""),)

    login_info = json.dumps(dict(username="Douglas", password="Callme2"))
    login_validation = json.dumps(dict(username="******", password="Callme2"))
    login_with_empty = json.dumps(dict(username="******", password="Callme2"))

    wrong_menu_fields = json.dumps(dict(thet="Breakfast", food="bans", price="2000", description="with milk"))
    same_food = json.dumps(dict(thetype="Breakfast", food="bans", price="2000", description="with milk"))
    add_meal = json.dumps(dict(thetype="Breakfast", food="bans", price="2000", description="with milk"))


    def setUp(self):
        '''Declaration of my setup file'''
        dbcon.create_tables()
        self.app = app.test_client(self)
        self.register_admin()
        self.register_attendant()


    def tearDown(self):
        '''function for deleting the database tables'''
        dbcon.delete_tables()


    def register_admin(self):
        '''creation of admin or owner'''
        obj = Attendant("admin", "admin", "admin", "admin")
        obj.add_attendant()
        

    def register_attendant(self):
        '''creation of attendant'''
        obj = Attendant("Douglas", "+256-755-598090", "Callme2", "attendant")
        obj.add_attendant()


    def attendant_login(self):
        response = self.app.post("/api/v2/auth/login",
            content_type='application/json',
            data=json.dumps(dict(attendant_name="katod", password="katod"))
        )
        reply = json.loads(response.data)
        return reply 


    def adminlogin(self):
        response = self.app.post("/api/v2/auth/login",
            content_type='application/json',
            data=json.dumps(dict(attendant_name="admin", password="admin"))
        )
        reply = json.loads(response.data)
        return reply 


if __name__ == '__main__':
    unittest.main()
