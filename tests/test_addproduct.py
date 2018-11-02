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
                                data=Testing.add_product   
                            )
        self.assertEqual(resp.status_code, 405)
        self.assertIn(b"Please put a valid URL", resp.data)


    def test_for_method_not_allowed(self):
        ''' test for method not allowed '''
        admin = self.adminlogin()
        resp = self.app.post("/api/v2/products/67878",
                                content_type='application/json', 
                                headers=dict(Authorization='Bearer '+admin['token']),
                                data=Testing.add_product   
                            )
        self.assertEqual(resp.status_code, 405)
        self.assertIn(b"Method not allowed", resp.data)


    def test_add_product_with_invalid_field(self):
        '''testing for invalid fields '''
        admin = self.adminlogin()
        resp = self.app.post("/api/v2/products",
                                content_type='application/json', 
                                headers=dict(Authorization='Bearer '+admin['token']),
                                data=Testing.wrong_pfields   
                            )
        self.assertEqual(resp.status_code, 400)
        self.assertIn(b"Some fields are missing, please check", resp.data)


    def test_add_product_successful(self):
        '''testing for successful '''
        admin = self.adminlogin()
        resp = self.app.post("/api/v2/products",
                                content_type='application/json', 
                                headers=dict(Authorization='Bearer '+admin['token']),
                                data=Testing.add_product   
                            )
        self.assertEqual(resp.status_code, 201)
        self.assertIn(b"You have successfully added Cookies", resp.data)


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


    # def test_deleting_product(self):
    #     admin = self.adminlogin()
    #     # resp = self.app.post("/api/v2/products",
    #     #                      content_type='application/json', 
    #     #                      headers=dict(Authorization='Bearer '+admin['token']),
    #     #                      data=Testing.add_product   
    #     #                      )
    #     resp2 = self.app.delete("/api/v2/products/1",
    #                              content_type='application/json', 
    #                              headers=dict(Authorization='Bearer '+admin['token']),)
    #     self.assertEqual(resp2.status_code, 404)
    #     self.assertIn(b"Successfully deleted product", resp2.data)


    # def test_deleting_product_with_wrong_id(self):
    #     admin= self.adminlogin()
    #     # response = self.app.post("/api/v2/products",
    #     #                          content_type='application/json', headers=dict(Authorization='Bearer '+admin_login['token']),
    #     #                          data=json.dumps(dict(product="Life Jackets", quantity="20",unit_price="200"),)   
    #     #                      )
    #     resp2 = self.app.delete("/api/v2/products/e",
    #                                 content_type='application/json', 
    #                                 headers=dict(Authorization='Bearer '+admin['token']),)                 
    #     self.assertEqual(resp2.status_code, 400)
    #     self.assertIn(b"No products with that id", resp2.data)
