from tests.test_base import Testing
from run import app
from flask import jsonify, json


class TestProduct(Testing):

    def test_for_invalid_url(self):
        '''testing for invalid url '''
        admin = self.adminlogin()
        resp = self.app.post("/api/v2/pr",
                                content_type='application/json', 
                                headers=dict(Authorization='Bearer '+admin['token']),
                                data=Testing.add_product )
        self.assertEqual(resp.status_code, 405)
        self.assertIn(b"Please put a valid URL", resp.data)


    def test_for_method_not_allowed(self):
        ''' test for method not allowed '''
        admin = self.adminlogin()
        resp = self.app.post("/api/v2/products/67878",
                                content_type='application/json', 
                                headers=dict(Authorization='Bearer '+admin['token']),
                                data=Testing.add_product )
        self.assertEqual(resp.status_code, 405)
        self.assertIn(b"Method not allowed", resp.data)


    def test_add_product_with_invalid_field(self):
        '''testing for invalid fields '''
        admin = self.adminlogin()
        resp = self.app.post("/api/v2/products",
                                content_type='application/json', 
                                headers=dict(Authorization='Bearer '+admin['token']),
                                data=Testing.wrong_pfields)
        self.assertEqual(resp.status_code, 400)
        self.assertIn(b"Some fields are missing, please check", resp.data)


    def test_add_product_successful(self):
        '''testing for successful '''
        admin = self.adminlogin()
        resp = self.app.post("/api/v2/products",
                                content_type='application/json', 
                                headers=dict(Authorization='Bearer '+admin['token']),
                                data=Testing.add_product )
        self.assertEqual(resp.status_code, 201)
        self.assertIn(b"You have successfully added Cookies", resp.data)

    
    def test_add_product_with_empty_name(self):
        '''testing for sapace '''
        admin = self.adminlogin()
        resp = self.app.post("/api/v2/products",
                                content_type='application/json', 
                                headers=dict(Authorization='Bearer '+admin['token']),
                                data=Testing.empty_pname)
        self.assertEqual(resp.status_code, 400)
        self.assertIn(b"Product name is missing", resp.data)


    def test_add_product_with_empty_price(self):
        '''testing for sapace '''
        admin = self.adminlogin()
        resp = self.app.post("/api/v2/products",
                                content_type='application/json', 
                                headers=dict(Authorization='Bearer '+admin['token']),
                                data=Testing.empty_price )
        self.assertEqual(resp.status_code, 400)
        self.assertIn(b"Unit_price is missing", resp.data)


    def test_add_product_with_empty_quabtity(self):
        '''testing for sapace '''
        admin = self.adminlogin()
        resp = self.app.post("/api/v2/products",
                                content_type='application/json', 
                                headers=dict(Authorization='Bearer '+admin['token']),
                                data=Testing.empty_quantity )
        self.assertEqual(resp.status_code, 400)
        self.assertIn(b"Quantity is missing", resp.data)


    def test_add_product_with_empty_category(self):
        '''testing for sapace '''
        admin = self.adminlogin()
        resp = self.app.post("/api/v2/products",
                                content_type='application/json', 
                                headers=dict(Authorization='Bearer '+admin['token']),
                                data=Testing.empty_category)
        self.assertEqual(resp.status_code, 400)
        self.assertIn(b"Category is missing", resp.data)


    def test_add_product_with_bad_name(self):
        '''testing for bad name '''
        admin = self.adminlogin()
        resp = self.app.post("/api/v2/products",
                                content_type='application/json', 
                                headers=dict(Authorization='Bearer '+admin['token']),
                                data=Testing.wrong_name)
        self.assertEqual(resp.status_code, 400)
        self.assertIn(b"Product name should be one or two words of 5 or more characters each", resp.data)


    def test_add_product_with_bad_price(self):
        '''testing for bad quantity '''
        admin = self.adminlogin()
        resp = self.app.post("/api/v2/products",
                                content_type='application/json', 
                                headers=dict(Authorization='Bearer '+admin['token']),
                                data=Testing.wrong_price)
        self.assertEqual(resp.status_code, 400)
        self.assertIn(b"Unit_price should have no spaces, be 3 or more integers and be in numbers", resp.data)


    def test_add_product_with_bad_quantity(self):
        '''testing for bad quantity '''
        admin = self.adminlogin()
        resp = self.app.post("/api/v2/products",
                                content_type='application/json', 
                                headers=dict(Authorization='Bearer '+admin['token']),
                                data=Testing.wrong_quantity)
        self.assertEqual(resp.status_code, 400)
        self.assertIn(b"Quantity should have no spaces and be in numbers", resp.data)


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
                                data=Testing.add_product  
                            )
        resp = self.app.post("/api/v2/products",
                                    content_type='application/json', 
                                    headers=dict(Authorization='Bearer '+admin['token']),
                                    data=Testing.add_product   
                                )                      
        self.assertEqual(resp.status_code, 400)
        self.assertIn(b"Product already exists, just update the quantity", resp.data)


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


    def test_deleting_product(self):
        admin = self.adminlogin()
        resp = self.app.post("/api/v2/products",
                             content_type='application/json', 
                             headers=dict(Authorization='Bearer '+admin['token']),
                             data=Testing.add_product   
                             )
        resp2 = self.app.delete("/api/v2/products/1",
                                 content_type='application/json', 
                                 headers=dict(Authorization='Bearer '+admin['token']),)
        self.assertEqual(resp2.status_code, 200)
        self.assertIn(b"Successfully deleted product", resp2.data)


    def test_deleting_product_with_wrong_id(self):
        admin= self.adminlogin()
        resp = self.app.post("/api/v2/products",
                                 content_type='application/json', headers=dict(Authorization='Bearer '+admin['token']),
                                 data=json.dumps(dict(product="Life Jackets", quantity="20",unit_price="200"),)   
                             )
        resp2 = self.app.delete("/api/v2/products/1234567890",
                                    content_type='application/json', 
                                    headers=dict(Authorization='Bearer '+admin['token']),)                 
        self.assertEqual(resp2.status_code, 404)
        self.assertIn(b"No products with that id", resp2.data)
