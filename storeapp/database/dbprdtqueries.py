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
        dbcon.cursor.execute(query, (productId,))
        deleted_row = dbcon.cursor.rowcount
        return deleted_row


    def update_one_product(self, quantity, productId):
        '''method that updatess one product from the database'''
        query = """UPDATE products SET quantity = %s  WHERE productId = %s"""
        dbcon.cursor.execute(query, (productId, quantity,))
        updated_row = dbcon.cursor.rowcount
        return updated_row


    def update_product_price(self, unit_price, productId):
        '''method that deletes one product from the database'''
        query = """UPDATE products SET unit_price = %s  WHERE productId = %s"""
        dbcon.cursor.execute(query, (productId, unit_price,))
        updated_row = dbcon.cursor.rowcount
        return updated_row
