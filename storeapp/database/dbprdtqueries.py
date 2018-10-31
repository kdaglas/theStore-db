from storeapp.database.dbconnector import DatabaseConnection
from storeapp.models.product_model import Product
import psycopg2
import psycopg2.extras as dictionary


dbcon = DatabaseConnection()

class DatabaseQueries():

    '''these are methods to perform certain queries to the database'''
    def get_product_by_name(self, product_name):
        '''method that checks for same product name in the database'''
        query = """SELECT * FROM products WHERE product_name = %s"""
        dbcon.cursor.execute(query, (product_name,))
        product = dbcon.cursor.fetchone()
        return product


    def fetch_all_products(self):
        '''method that retieves all the product from the database'''
        query = """SELECT * FROM products"""
        dbcon.cursor.execute(query)
        products = dbcon.cursor.fetchall()
        return products


    def fetch_one_product(self, productId):
        '''method that retieves one product from the database'''
        query = """SELECT * FROM products WHERE productId = %s"""
        dbcon.cursor.execute(query, (productId,))
        product = dbcon.cursor.fetchone()
        return product
