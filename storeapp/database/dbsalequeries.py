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
    def create_sales_record(self, productId, quantity):
        
        existing_product = dbquery.fetch_one_product(productId)
        if existing_product is None:
            return False
        if existing_product["quantity"] < int(quantity):
            return False
        product_name = existing_product["product_name"]
        quantity = int(quantity)
        pay_amount = (existing_product["unit_price"]*int(quantity))
        attendant_name = get_jwt_identity()
        new_sale = SaleRecord(product_name, quantity, pay_amount, attendant_name)
        SaleRecord.create_sale_record(new_sale.product_name,
                                        new_sale.quantity,
                                        new_sale.pay_amount, 
                                        new_sale.attendant_name)
        new_quantity = int(existing_product["quantity"]) - quantity
        updated_sale = dbquery.update_one_product(productId, new_quantity)
        return updated_sale
            


    def fetch_all_sale_records(self):
        '''method that retieves all the sale records from the database'''
        query = """SELECT * FROM salerecords"""
        dbcon.cursor.execute(query)
        products = dbcon.cursor.fetchall()
        return products


    def fetch_one_sale_record(self, saleId):
        '''method that retieves one sale record from the database'''
        query = """SELECT * FROM salerecords WHERE saleId = %s"""
        dbcon.cursor.execute(query, (saleId,))
        sale_record = dbcon.cursor.fetchone()
        return sale_record
