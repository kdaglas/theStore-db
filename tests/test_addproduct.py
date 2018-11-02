from tests.test_base import Testing
from run import app
from flask import jsonify, json


class TestProduct(Testing):

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
