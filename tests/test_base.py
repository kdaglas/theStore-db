import unittest
import json
from storeapp import app
from storeapp.database.dbconnector import DatabaseConnection
from storeapp.models.user_model import Attendant


dbcon = DatabaseConnection()

class Testing(unittest.TestCase):

    ''' data for success '''
    login_info = json.dumps(dict(attendant_name="admin", password="Admin17"),)
    registering_attendant = json.dumps(dict(attendant_name="Douglas", contact="+256-755-598090", password="Callme2", role="attendant"),)
    add_product = json.dumps(dict(product_name="Cookies", unit_price="800", quantity="20", category="foodish"),)
    create_sales = json.dumps(dict(product_name="Cookies", quantity="20", pay_amount="800", attendant_name="admin"),)

    ''' data for login validation '''
    login_invalid_name = json.dumps(dict(attendant_name="Chuc", password="Chuck17"),)

    ''' data for wrong fields '''
    wrong_lfields = json.dumps(dict(attendant="admin", password="Admin17"),)
    wrong_afields = json.dumps(dict(attendant="Douglas", contact="+256-755-598090", password="Callme2", role="attendant"),)
    wrong_pfields = json.dumps(dict(product="Cookies", unit_price="800", quantity="20", category="foodish"),)
    wrong_sfields = json.dumps(dict(product="Cookies", quantity="20", pay_amount="800", attendant_name="admin"),)
    wrong_ufields = json.dumps(dict(attendant_name="Douglas", contact="+256-755-598090", password="Callme2", roles="admin"),)

    ''' data for attendant '''
    empty_aname = json.dumps(dict(attendant_name="", contact="+256-755-598090", password="Callme2", role="attendant"),)
    empty_contact = json.dumps(dict(attendant_name="Douglas", contact="", password="Callme2", role="attendant"),)
    empty_password = json.dumps(dict(attendant_name="Douglas", contact="+256-755-598090", password="", role="attendant"),)
    wrong_password = json.dumps(dict(attendant_name="Douglas", contact="+256-755-598090", password="Callme2456tgfd", role="attendant"),)
    wrong_anme = json.dumps(dict(attendant_name="555", contact="+256-755-598090", password="Callme2", role="attendant"),)
    wrong_contact = json.dumps(dict(attendant_name="Douglas", contact="256755598090", password="Callme2", role="attendant"),)
    '''("chuck", "+256-755-555555", "Chuck17", "attendant")'''
    dupliate_contact = json.dumps(dict(attendant_name="Douglas", contact="+256-755-555555", password="Callie5", role="attendant"),)
    dupliate_name = json.dumps(dict(attendant_name="chuck", contact="+256-755-598090", password="Callie5", role="attendant"),)

    update_user = json.dumps(dict(attendant_name="Douglas", contact="+256-755-598090", password="Callme2", role="admin"),)
    update_wrong_role = json.dumps(dict(attendant_name="Douglas", contact="+256-755-598090", password="Callme2", role="admininistrator"),)
    

    ''' data for product validation '''
    empty_pname = json.dumps(dict(product_name="", unit_price="800", quantity="20", category="foodish"),)
    empty_price = json.dumps(dict(product_name="Cookies", unit_price="", quantity="20", category="foodish"),)
    empty_quantity = json.dumps(dict(product_name="Cookies", unit_price="800", quantity="", category="foodish"),)
    empty_category = json.dumps(dict(product_name="Cookies", unit_price="800", quantity="20", category=""),)
    wrong_name = json.dumps(dict(product_name="Cook123", unit_price="800", quantity="20", category="foodish"),)
    wrong_price = json.dumps(dict(product_name="Cookies", unit_price="mee", quantity="20", category="foodish"),)
    wrong_quantity = json.dumps(dict(product_name="Cookies", unit_price="800", quantity="mee", category="foodish"),)
    wrong_category = json.dumps(dict(product_name="Cookies", unit_price="800", quantity="20", category="12345"),)
    zero_price = json.dumps(dict(product_name="Cookies", unit_price="0", quantity="20", category="foodish"),)
    zero_quantity = json.dumps(dict(product_name="Cookies", unit_price="800", quantity="0", category="foodish"),)

    ''' data for sales validation '''



    def setUp(self):
        '''Declaration of my setup file'''
        dbcon.create_tables()
        self.app = app.test_client(self)
        self.register_admin()
        self.register_attendant()


    def tearDown(self):
        '''function for deleting the database tables'''
        dbcon.delete_tables()


    def register_attendant(self):
        '''creation of attendant'''
        registeered = Attendant("chuck", "+256-755-555555", "Chuck17", "attendant")
        registeered.add_attendant()


    def attendantlogin(self):
        resp = self.app.post("/api/v2/auth/login",
                             data=json.dumps(dict(attendant_name="Chuck", password="Chuck17"),),
                             content_type='application/json'
                            )
        reply = json.loads(resp.data)
        return reply 


    def register_admin(self):
        '''creation of admin or owner'''
        registered = Attendant("admin", "+256-700-000000", "Admin17", "admin")
        registered.add_attendant()
        

    def adminlogin(self):
        resp = self.app.post("/api/v2/auth/login",
                             data=json.dumps(dict(attendant_name="admin", password="Admin17"),),
                             content_type='application/json' 
                            )
        reply = json.loads(resp.data)
        return reply 


if __name__ == '__main__':
    unittest.main()
