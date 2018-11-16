'''Packages for the required models'''
from storeapp.database.dbconnector import DatabaseConnection
import psycopg2
import psycopg2.extras as dictionary
from storeapp import app


dbcon = DatabaseConnection()

class Product():

    def __init__(self, product_name, unit_price, quantity, category):
        '''Declaring all the parameters'''
        self.product_name = product_name
        self.unit_price = unit_price
        self.quantity = quantity
        self.category = category

    def add_product(self):
        '''method that adds a product to the database'''
        query = """INSERT INTO products(product_name, unit_price, quantity, category) 
                    VALUES (%s, %s, %s, %s)"""
        dbcon.cursor.execute(query, (self.product_name, self.unit_price, self.quantity, self.category))
        return  "You have successfully added {}".format(self.product_name)
