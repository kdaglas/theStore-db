from tests.test_base import Testing
from run import app
from flask import jsonify, json


class TestProduct(Testing):

    '''the test on the add product route'''

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
        '''test invalid fields '''
        admin = self.adminlogin()
        resp = self.app.post("/api/v2/products",
                             content_type='application/json', 
                             headers=dict(Authorization='Bearer '+admin['token']),
                             data=Testing.wrong_pfields)
        self.assertEqual(resp.status_code, 400)
        self.assertIn(b"Some fields are missing, please check", resp.data)

    # def test_add_user_with_user_logged_in(self):
    #     '''testing for user authentication '''
    #     attendant = self.attendantlogin()
    #     resp = self.app.post("/api/v2/products",
    #                          content_type='application/json', 
    #                          headers=dict(Authorization='Bearer '+attendant['token']),
    #                          data=Testing.add_product)
    #     self.assertEqual(resp.status_code, 401)
    #     self.assertIn(b"Unauthorized to operate this feature", resp.data)

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
        self.assertIn(b"Some input value are missing, recheck", resp.data)

    def test_add_product_with_empty_price(self):
        '''testing for sapace '''
        admin = self.adminlogin()
        resp = self.app.post("/api/v2/products",
                             content_type='application/json', 
                             headers=dict(Authorization='Bearer '+admin['token']),
                             data=Testing.empty_price )
        self.assertEqual(resp.status_code, 400)
        self.assertIn(b"Some input value are missing, recheck", resp.data)

    def test_add_product_with_empty_quantity(self):
        '''testing for sapace '''
        admin = self.adminlogin()
        resp = self.app.post("/api/v2/products",
                             content_type='application/json', 
                             headers=dict(Authorization='Bearer '+admin['token']),
                             data=Testing.empty_quantity )
        self.assertEqual(resp.status_code, 400)
        self.assertIn(b"Some input value are missing, recheck", resp.data)

    def test_add_product_with_empty_category(self):
        '''testing for sapace '''
        admin = self.adminlogin()
        resp = self.app.post("/api/v2/products",
                             content_type='application/json', 
                             headers=dict(Authorization='Bearer '+admin['token']),
                             data=Testing.empty_category)
        self.assertEqual(resp.status_code, 400)
        self.assertIn(b"Some input value are missing, recheck", resp.data)

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
        '''testing for bad price '''
        admin = self.adminlogin()
        resp = self.app.post("/api/v2/products",
                             content_type='application/json', 
                             headers=dict(Authorization='Bearer '+admin['token']),
                             data=Testing.wrong_price)
        self.assertEqual(resp.status_code, 400)
        self.assertIn(b"Some fields are missing, please check", resp.data)

    def test_add_product_with_bad_quantity(self):
        '''testing for bad quantity '''
        admin = self.adminlogin()
        resp = self.app.post("/api/v2/products",
                             content_type='application/json', 
                             headers=dict(Authorization='Bearer '+admin['token']),
                             data=Testing.wrong_quantity)
        self.assertEqual(resp.status_code, 400)
        self.assertIn(b"Some fields are missing, please check", resp.data)

    def test_add_product_with_zero_price(self):
        '''testing for bzero '''
        admin= self.adminlogin()
        resp = self.app.post("/api/v2/products",
                             content_type='application/json', 
                             headers=dict(Authorization='Bearer '+admin['token']),
                             data=Testing.zero_price)   
        self.assertEqual(resp.status_code, 400)
        self.assertIn(b"Unit_price and quantity should be more than 0", resp.data)   

    def test_add_product_with_zero_quantiyty(self):
        '''testing for zero '''
        admin= self.adminlogin()
        resp = self.app.post("/api/v2/products",
                             content_type='application/json', 
                             headers=dict(Authorization='Bearer '+admin['token']),
                             data=Testing.zero_quantity)   
        self.assertEqual(resp.status_code, 400)
        self.assertIn(b"Unit_price and quantity should be more than 0", resp.data)  

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



    '''tests for the fetching 
        all route for products'''

    def test_for_fetching_empty_product_table(self):
        '''test for fetching all products that dont exist'''
        admin = self.adminlogin()
        resp = self.app.get("/api/v2/products",
                             content_type='application/json', 
                             headers=dict(Authorization='Bearer '+admin['token']),)              
        self.assertEqual(resp.status_code, 404)
        self.assertIn(b"No products added yet", resp.data)

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



    '''tests for the fetching 
        one route for product'''

    def test_wrong_id(self):
        '''test for getting one '''
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

    def test_for_fetching_empty_product(self):
        '''test for fetching an empty that dont exist'''
        admin = self.adminlogin()
        resp = self.app.get("/api/v2/products/1",
                             content_type='application/json', 
                             headers=dict(Authorization='Bearer '+admin['token']),)
        self.assertEqual(resp.status_code, 404)
        self.assertIn(b"No product with that id", resp.data)

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

    

    '''tests update route for product'''

    def test_update_wrong_id(self):
        '''test for getting one '''
        admin = self.adminlogin()
        resp = self.app.post("/api/v2/products",
                             content_type='application/json', 
                             headers=dict(Authorization='Bearer '+admin['token']),
                             data=Testing.add_product)
        resp2 = self.app.put("/api/v2/products/a",
                             content_type='application/json', 
                             headers=dict(Authorization='Bearer '+admin['token']),
                             data=Testing.update_product)
        self.assertEqual(resp2.status_code, 400)
        self.assertIn(b"Id input should be an integer", resp2.data)

    def test_update_empty(self):
        '''test for updating with empty '''
        admin = self.adminlogin()
        resp = self.app.post("/api/v2/products",
                             content_type='application/json', 
                             headers=dict(Authorization='Bearer '+admin['token']),
                             data=Testing.add_product)
        resp2 = self.app.put("/api/v2/products/1",
                             content_type='application/json', 
                             headers=dict(Authorization='Bearer '+admin['token']),
                             data=Testing.update_empty_price)
        self.assertEqual(resp2.status_code, 400)
        self.assertIn(b"Unit price or quantity is missing", resp2.data)

    def test_update_empty_quantity(self):
        '''test for updating with empty '''
        admin = self.adminlogin()
        resp = self.app.post("/api/v2/products",
                             content_type='application/json', 
                             headers=dict(Authorization='Bearer '+admin['token']),
                             data=Testing.add_product)
        resp2 = self.app.put("/api/v2/products/1",
                             content_type='application/json', 
                             headers=dict(Authorization='Bearer '+admin['token']),
                             data=Testing.update_empty_quantity)
        self.assertEqual(resp2.status_code, 400)
        self.assertIn(b"Unit price or quantity is missing", resp2.data)

    def test_update_product_with_bad_price(self):
        '''testing for bad price '''
        admin = self.adminlogin()
        resp = self.app.post("/api/v2/products",
                             content_type='application/json', 
                             headers=dict(Authorization='Bearer '+admin['token']),
                             data=Testing.add_product)
        resp = self.app.put("/api/v2/products/1",
                             content_type='application/json', 
                             headers=dict(Authorization='Bearer '+admin['token']),
                             data=Testing.update_wrong_price)
        self.assertEqual(resp.status_code, 400)
        self.assertIn(b"Some fields are missing, please check", resp.data)

    def test_update_product_with_bad_quantity(self):
        '''testing for bad quantity '''
        admin = self.adminlogin()
        resp = self.app.post("/api/v2/products",
                             content_type='application/json', 
                             headers=dict(Authorization='Bearer '+admin['token']),
                             data=Testing.add_product)
        resp = self.app.put("/api/v2/products/1",
                             content_type='application/json', 
                             headers=dict(Authorization='Bearer '+admin['token']),
                             data=Testing.update_wrong_quantity)
        self.assertEqual(resp.status_code, 400)
        self.assertIn(b"Some fields are missing, please check", resp.data)

    def test_update_product_with_zero_price(self):
        '''testing for bzero '''
        admin= self.adminlogin()
        resp = self.app.post("/api/v2/products",
                             content_type='application/json', 
                             headers=dict(Authorization='Bearer '+admin['token']),
                             data=Testing.add_product)
        resp = self.app.put("/api/v2/products/1",
                             content_type='application/json', 
                             headers=dict(Authorization='Bearer '+admin['token']),
                             data=Testing.update_zero_price)   
        self.assertEqual(resp.status_code, 400)
        self.assertIn(b"Unit_price and quantity should be more than 0", resp.data)   

    def test_update_product_with_zero_quantiyty(self):
        '''testing for zero '''
        admin= self.adminlogin()
        resp = self.app.post("/api/v2/products",
                             content_type='application/json', 
                             headers=dict(Authorization='Bearer '+admin['token']),
                             data=Testing.add_product)
        resp = self.app.put("/api/v2/products/1",
                             content_type='application/json', 
                             headers=dict(Authorization='Bearer '+admin['token']),
                             data=Testing.update_zero_quantity)   
        self.assertEqual(resp.status_code, 400)
        self.assertIn(b"Unit_price and quantity should be more than 0", resp.data)



    '''testing delete route for product'''

    def test_wrong_id_for_one(self):
        '''test for deletin '''
        admin = self.adminlogin()
        resp = self.app.post("/api/v2/products",
                             content_type='application/json', 
                             headers=dict(Authorization='Bearer '+admin['token']),
                             data=Testing.add_product)
        resp2 = self.app.delete("/api/v2/products/a",
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
        self.assertIn(b"No product with that id", resp2.data)


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
        self.assertIn(b"No product with that id", resp2.data)
