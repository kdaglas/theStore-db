from storeapp.database.dbconnector import DatabaseConnection
from storeapp.database.dbprdtqueries import DatabaseQueries
from storeapp.models.sale_model import SaleRecord
import psycopg2
import psycopg2.extras as dictionary
from flask import request, jsonify, json


dbcon = DatabaseConnection()
dbquery = DatabaseQueries()

class SaleDatabaseQueries():

    '''these are methods to perform certain queries to the database'''
    def create_sales_record(self, productId, quantity):
        
        existing_product = dbquery.fetch_one_product(productId)
        if existing_product["quantity"] > int(quantity):
            product = existing_product["product_name"]
            quantity = int(quantity)
            pay_amount = (existing_product["unit_price"]*int(quantity))
            attendant = attendant
            new_sale = Sale(product_name=product, quantity=_quantity,
                            unit_price=amount, attendant=_attendant, date=_date)
            self.dbcon.create_sale_record(product=new_sale.product_name, quantity=new_sale.quantity,
                                        amount=new_sale.unit_price, attendant=new_sale.attendant, date=new_sale.date)
            new_quantity = int(item["quantity"])- _quantity
            self.dbcon.update_product(product=product, quantity=new_quantity, unit_price=item["unit_price"], product_id=product_id)
            return True
        else:
            return False
        


    def authenticate_attendant(self, attendant_name, password):
        '''method for logging in an attendant'''
        query = """SELECT attendant_name, password FROM attendants WHERE attendant_name = %s and password = %s"""
        dbcon.cursor.execute(query, (attendant_name, password,))
        login = dbcon.cursor.fetchone()
        return login


    def get_attendant_by_name(self, attendant_name):
        '''method to return an attendant by name the db'''
        query = """SELECT * FROM attendants WHERE attendant_name = %s"""
        dbcon.cursor.execute(query, (attendant_name,))
        attendant = dbcon.cursor.fetchone()
        return attendant


    def get_attendant_by_contact(self, contact):
        '''method that checks if attendant contact is already added in the database'''
        query = """SELECT * FROM attendants WHERE contact = %s"""
        dbcon.cursor.execute(query, (contact,))
        attendant = dbcon.cursor.fetchone()
        return attendant


    def promote_to_admin(self, role, attendantId):
        '''this method returns the new admin'''
        query = """UPDATE attendants SET role = %s WHERE attendantId = %s"""
        dbcon.cursor.execute(query, (attendantId, role,))


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


    def update_one_product(self, quantity, productId):
        '''method that deletes one product from the database'''
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
