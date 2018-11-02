# from tests.test_base import Testing
# from run import app
# from flask import jsonify, json
# from storeapp.database.dbconnector import DatabaseConnection


# dbcon = DatabaseConnection()

# class TestUser(Testing):

#     def setUp(self):
#         self.app = app.test_client()
#         dbcon.create_tables()


#     def test_add_attenadnt_with_invalid_fields(self):
#         login = self.admin_login
#         '''test adding attendant with invalid fields'''
#         response = self.app.post('/api/v2/auth/signup', data = Testing.wrong_fields,
#                                 content_type="application/json")
#         self.assertEqual(response.status_code, 400)
#         self.assertIn(b"Some fields are missing, please check", response.data)


    # def test_register_customer_with_same_contact(self):
    #     '''test registering a customer with same contact'''
    #     response = self.app.post('/api/v2/auth/signup', data = Testing.same_contact,
    #                             content_type="application/json")
    #     self.assertEqual(response.status_code, 400)
