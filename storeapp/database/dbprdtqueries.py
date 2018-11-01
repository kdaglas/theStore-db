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


    def delete_one_product(self, productId):
        '''method that deletes one product from the database'''
        query = """DELETE FROM products WHERE productId = %s"""
        deleted_row = dbcon.cursor.rowcount
        dbcon.cursor.execute(query, (productId,))
        return deleted_row


    def update_one_product(self, unit_price, quantity, productId):
        '''method that deletes one product from the database'''
        query = """UPDATE products SET unit_price = %s, quantity = %s WHERE productId = %s"""
        updated_row = dbcon.cursor.rowcount
        dbcon.cursor.execute(query, (productId, unit_price, quantity,))
        return updated_row
