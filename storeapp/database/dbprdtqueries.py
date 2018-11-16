from storeapp.database.dbconnector import DatabaseConnection
from storeapp.models.product_model import Product
import psycopg2
import psycopg2.extras as dictionary


dbcon = DatabaseConnection()

class ProductDatabaseQueries():

    '''these are methods to perfrmm certain queriey to the database'''
    def get_product_by_name(self, product_name):
        '''method that checks for same product name in the database'''
        query = """SELECT * FROM products WHERE product_name = %s"""
        dbcon.cursor.execute(query, (product_name,))
        product = dbcon.cursor.fetchone()
        return product


    def fetch_all_products(self):
        '''retieving all the product'''
        query = """SELECT * FROM products"""
        dbcon.cursor.execute(query)
        products = dbcon.cursor.fetchall()
        return products


    def fetch_one_product(self, productId):
        '''get one product from the db'''
        query = """SELECT * FROM products WHERE productId = %s"""
        dbcon.cursor.execute(query, (productId,))
        product = dbcon.cursor.fetchone()
        return product


    def update_product(self, unit_price, quantity, productId):
        '''method that updates price of one product'''
        query = """UPDATE products SET unit_price = %s, quantity = %s  WHERE productId = %s"""
        dbcon.cursor.execute(query, (unit_price, quantity, productId,))
        updated_row = dbcon.cursor.rowcount
        return updated_row


    def delete_one_product(self, productId):
        '''deletes one'''
        query = """DELETE FROM products WHERE productId = %s"""
        dbcon.cursor.execute(query, (productId,))
        deleted_row = dbcon.cursor.rowcount
        return deleted_row
