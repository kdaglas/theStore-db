from tests.test_base import Testing
from run import app
from flask import jsonify, json


class TestAttendant(Testing):

    def test_for_invalid_url(self):
        '''testing for invalid url '''
        admin = self.adminlogin()
        resp = self.app.post("/api/v2/auth/sign",
                             content_type='application/json', 
                             headers=dict(Authorization='Bearer '+admin['token']),
                             data=Testing.registering_attendant )
        self.assertEqual(resp.status_code, 405)
        self.assertIn(b"Please put a valid URL", resp.data)


    def test_for_method_not_allowed(self):
        ''' test for method not allowed '''
        admin = self.adminlogin()
        resp = self.app.post("/api/v2/auth/signup/76446",
                             content_type='application/json', 
                             headers=dict(Authorization='Bearer '+admin['token']),
                             data=Testing.registering_attendant )
        self.assertEqual(resp.status_code, 405)
        self.assertIn(b"Method not allowed", resp.data)


    def test_add_product_with_invalid_field(self):
        '''testing for invalid fields '''
        admin = self.adminlogin()
        resp = self.app.post("/api/v2/auth/signup",
                             content_type='application/json', 
                             headers=dict(Authorization='Bearer '+admin['token']),
                             data=Testing.wrong_afields)
        self.assertEqual(resp.status_code, 400)
        self.assertIn(b"Some fields are missing, please check", resp.data)


    # def test_user_reg_successful(self):
    #     '''testing for successful '''
    #     admin = self.adminlogin()
    #     resp = self.app.post("/api/v2/auth/signup",
    #                          content_type='application/json', 
    #                          headers=dict(Authorization='Bearer '+admin['token']),
    #                          data=Testing.registering_attendant )
    #     self.assertEqual(resp.status_code, 201)
    #     self.assertIn(b"You have successfully added Douglas", resp.data)

    
    def test_add_user_with_empty_name(self):
        '''testing for space '''
        admin = self.adminlogin()
        resp = self.app.post("/api/v2/auth/signup",
                                content_type='application/json', 
                                headers=dict(Authorization='Bearer '+admin['token']),
                                data=Testing.empty_aname)
        self.assertEqual(resp.status_code, 400)
        self.assertIn(b"Username is missing", resp.data)


    # def test_add_user_with_empty_contact(self):
    #     '''testing for sapace '''
    #     admin = self.adminlogin()
    #     resp = self.app.post("/api/v2/products",
    #                             content_type='application/json', 
    #                             headers=dict(Authorization='Bearer '+admin['token']),
    #                             data=Testing.empty_contact)
    #     self.assertEqual(resp.status_code, 400)
    #     self.assertIn(b"Contact is missing", resp.data)


    def test_add_product_with_empty_password(self):
        '''testing for sapace '''
        admin = self.adminlogin()
        resp = self.app.post("/api/v2/auth/signup",
                                content_type='application/json', 
                                headers=dict(Authorization='Bearer '+admin['token']),
                                data=Testing.empty_password)
        self.assertEqual(resp.status_code, 400)
        self.assertIn(b"Password is missing", resp.data)


    # def test_add_product_with_empty_category(self):
    #     '''testing for sapace '''
    #     admin = self.adminlogin()
    #     resp = self.app.post("/api/v2/products",
    #                             content_type='application/json', 
    #                             headers=dict(Authorization='Bearer '+admin['token']),
    #                             data=Testing.empty_category)
    #     self.assertEqual(resp.status_code, 400)
    #     self.assertIn(b"Category is missing", resp.data)


    def test_add_product_with_bad_name(self):
        '''testing for bad name '''
        admin = self.adminlogin()
        resp = self.app.post("/api/v2/auth/signup",
                                content_type='application/json', 
                                headers=dict(Authorization='Bearer '+admin['token']),
                                data=Testing.wrong_anme)
        self.assertEqual(resp.status_code, 400)
        self.assertIn(b"Username should be one or two words of 5 or more characters each", resp.data)


    # def test_add_product_with_bad_price(self):
    #     '''testing for bad price '''
    #     admin = self.adminlogin()
    #     resp = self.app.post("/api/v2/products",
    #                             content_type='application/json', 
    #                             headers=dict(Authorization='Bearer '+admin['token']),
    #                             data=Testing.wrong_price)
    #     self.assertEqual(resp.status_code, 400)
    #     self.assertIn(b"Unit_price should have no spaces, be 3 or more integers and be in numbers", resp.data)


    # def test_add_product_with_bad_quantity(self):
    #     '''testing for bad quantity '''
    #     admin = self.adminlogin()
    #     resp = self.app.post("/api/v2/products",
    #                             content_type='application/json', 
    #                             headers=dict(Authorization='Bearer '+admin['token']),
    #                             data=Testing.wrong_quantity)
    #     self.assertEqual(resp.status_code, 400)
    #     self.assertIn(b"Quantity should have no spaces and be in numbers", resp.data)


    def test_add_product_with_zero_price(self):
        '''testing for bzero '''
        admin= self.adminlogin()
        resp = self.app.post("/api/v2/products",
                                 content_type='application/json', 
                                 headers=dict(Authorization='Bearer '+admin['token']),
                                 data=Testing.zero_price)   
        self.assertEqual(resp.status_code, 400)
        self.assertIn(b"Unit_price should be more than 0", resp.data)   


    def test_add_product_with_zero_quantiyty(self):
        '''testing for zero '''
        admin= self.adminlogin()
        resp = self.app.post("/api/v2/products",
                                 content_type='application/json', 
                                 headers=dict(Authorization='Bearer '+admin['token']),
                                 data=Testing.zero_quantity)   
        self.assertEqual(resp.status_code, 400)
        self.assertIn(b"Quantity should be more than 0", resp.data)  


    def test_add_product_with_bad_category(self):
        '''testing for bad category'''
        admin = self.adminlogin()
        resp = self.app.post("/api/v2/products",
                                content_type='application/json', 
                                headers=dict(Authorization='Bearer '+admin['token']),
                                data=Testing.wrong_category)
        self.assertEqual(resp.status_code, 400)
        self.assertIn(b"Category should be 5 or more characters and be in characters", resp.data)


    def test_adding_existing_product(self):
        '''testing for duplicate data '''
        admin= self.adminlogin()
        resp1 = self.app.post("/api/v2/products",
                                content_type='application/json', 
                                headers=dict(Authorization='Bearer '+admin['token']),
                                data=Testing.add_product)
        resp = self.app.post("/api/v2/products",
                             content_type='application/json', 
                             headers=dict(Authorization='Bearer '+admin['token']),
                             data=Testing.add_product)                      
        self.assertEqual(resp.status_code, 400)
        self.assertIn(b"Product already exists, just update the quantity", resp.data)


    def test_fetching_products(self):
        '''testing for getting all products '''
        admin= self.adminlogin()
        resp1 = self.app.post("/api/v2/products",
                                content_type='application/json', 
                                headers=dict(Authorization='Bearer '+admin['token']),
                                data=Testing.add_product)
        resp = self.app.get("/api/v2/products",
                             content_type='application/json', 
                             headers=dict(Authorization='Bearer '+admin['token']),)                      
        self.assertEqual(resp.status_code, 200)
        self.assertIn(b"All products have been viewed", resp.data)


    def test_fetching_one_product(self):
        '''testing for getting 1 product '''
        admin= self.adminlogin()
        resp1 = self.app.post("/api/v2/products",
                                content_type='application/json', 
                                headers=dict(Authorization='Bearer '+admin['token']),
                                data=Testing.add_product)
        resp = self.app.get("/api/v2/products/1",
                             content_type='application/json', 
                             headers=dict(Authorization='Bearer '+admin['token']),)                      
        self.assertEqual(resp.status_code, 200)
        self.assertIn(b"Product has been viewed", resp.data)


    def test_for_fetching_empty_product_table(self):
        '''test for fetching all products that dont exist'''
        admin = self.adminlogin()
        resp = self.app.get("/api/v2/products",
                             content_type='application/json', 
                             headers=dict(Authorization='Bearer '+admin['token']),)              
        self.assertEqual(resp.status_code, 404)
        self.assertIn(b"No products added yet", resp.data)


    def test_for_fetching_empty_product(self):
        '''test for fetching an empty that dont exist'''
        admin = self.adminlogin()
        resp = self.app.get("/api/v2/products/1",
                             content_type='application/json', 
                             headers=dict(Authorization='Bearer '+admin['token']),)
        self.assertEqual(resp.status_code, 404)
        self.assertIn(b"No product with that id", resp.data)


    def test_wrong_id(self):
        '''test for deletin '''
        admin = self.adminlogin()
        resp = self.app.post("/api/v2/products",
                             content_type='application/json', 
                             headers=dict(Authorization='Bearer '+admin['token']),
                             data=Testing.add_product)
        resp2 = self.app.get("/api/v2/products/a",
                                 content_type='application/json', 
                                 headers=dict(Authorization='Bearer '+admin['token']),)
        self.assertEqual(resp2.status_code, 400)
        self.assertIn(b"Id input should be an integer", resp2.data)


    def test_deleting_product(self):
        '''test for deletin '''
        admin = self.adminlogin()
        resp = self.app.post("/api/v2/products",
                             content_type='application/json', 
                             headers=dict(Authorization='Bearer '+admin['token']),
                             data=Testing.add_product)
        resp2 = self.app.delete("/api/v2/products/1",
                                 content_type='application/json', 
                                 headers=dict(Authorization='Bearer '+admin['token']),)
        self.assertEqual(resp2.status_code, 200)
        self.assertIn(b"Successfully deleted product", resp2.data)


    def test_deleting_product_with_wrong_id(self):
        '''test for deletin with wrong id'''
        admin= self.adminlogin()
        resp = self.app.post("/api/v2/products",
                             content_type='application/json', headers=dict(Authorization='Bearer '+admin['token']),
                             data=Testing.add_product)
        resp2 = self.app.delete("/api/v2/products/1234567890",
                                 content_type='application/json', 
                                 headers=dict(Authorization='Bearer '+admin['token']),)                 
        self.assertEqual(resp2.status_code, 404)
        self.assertIn(b"No products with that id", resp2.data)


    def test_deleting_product_with_nothing(self):
        '''test for deletin with nothing'''
        admin= self.adminlogin()
        resp = self.app.post("/api/v2/products",
                             content_type='application/json', headers=dict(Authorization='Bearer '+admin['token']),
                             data=Testing.add_product)
        resp2 = self.app.delete("/api/v2/products/1234567890",
                                 content_type='application/json', 
                                 headers=dict(Authorization='Bearer '+admin['token']),)                 
        self.assertEqual(resp2.status_code, 404)
        self.assertIn(b"No products with that id", resp2.data)
