from storeapp.database.dbconnector import DatabaseConnection
from storeapp.database.dbprdtqueries import ProductDatabaseQueries
from storeapp.models.sale_model import SaleRecord
from flask_jwt_extended import create_access_token, get_jwt_identity
import psycopg2
import psycopg2.extras as dictionary
from flask import request, jsonify, json


dbcon = DatabaseConnection()
dbquery = ProductDatabaseQueries()

class SaleDatabaseQueries():

    '''these are methods to perform certain queries to the database'''
    def create_sales_record(self, productId, quantity, attendant_name):
        
        existing_product = dbquery.fetch_one_product(productId)
        if not existing_product:
            return False
        if existing_product["quantity"] > int(quantity):
            print('too much')
            product_name = existing_product["product_name"]
            quantity = int(quantity)
            pay_amount = (existing_product["unit_price"]*int(quantity))
            attendant_name = attendant_name
            new_sale = SaleRecord(product_name, quantity, pay_amount, attendant_name)
            SaleRecord.create_sale_record(new_sale.product_name,
                                            new_sale.quantity,
                                            new_sale.pay_amount, 
                                            new_sale.attendant_name)
            new_quantity = int(existing_product["quantity"]) - quantity
            updated_sale = dbquery.update_one_product(productId, new_quantity)
            return updated_sale
        return False   

    def fetch_all_sale_records(self):
        '''method that retieves all the sale records from the database'''
        query = """SELECT * FROM salerecords"""
        dbcon.cursor.execute(query)
        sale_records = dbcon.cursor.fetchall()
        return sale_records


    def fetch_one_sale_record(self, saleId):
        '''method that retieves one sale record from the database'''
        query = """SELECT * FROM salerecords WHERE saleId = %s"""
        dbcon.cursor.execute(query, (saleId,))
        sale_record = dbcon.cursor.fetchone()
        return sale_record


    def fetch_all_sale_records_by_name(self, attendant_name):
        '''method that retieves all sale records from the database of one user'''
        query = """SELECT * FROM salerecords WHERE attendant_name = %s"""
        dbcon.cursor.execute(query, (attendant_name,))
        sale_records = dbcon.cursor.fetchall()
        return sale_records
        

    def get_records_by_name(self, attendant_name):
        '''method to return an attendant by name the db'''
        query = """SELECT * FROM salerecords WHERE attendant_name = %s"""
        dbcon.cursor.execute(query, (attendant_name,))
        attendant = dbcon.cursor.fetchall()
        return attendant    
