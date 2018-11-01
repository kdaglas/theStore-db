from storeapp.database.dbconnector import DatabaseConnection
import psycopg2
import psycopg2.extras as dictionary
from storeapp import app


dbcon = DatabaseConnection()

'''Object classes for the sales model'''
class SaleRecord():

    def __init__(self, product_name, quantity, pay_amount, attendant_name):
        '''Declaring all the parameters'''
        self.product_name = product_name
        self.quantity = quantity
        self.pay_amount = pay_amount
        self.attendant_name = attendant_name

    
    # def create_sale_record(self):
    #     '''method that registers or adds a user to the database'''
    #     query = """INSERT INTO salerecords(product_name, quantity, pay_amount, attendant_name) 
    #                 VALUES (%s, %s, %s, %s)"""      
    #     dbcon.cursor.execute(query, (self.product_name, self.quantity, self.pay_amount, self.attendant_name))
    #     return  "You have made a sale record of {}".format(self.product_name)


    @staticmethod
    def create_sale_record(product_name, quantity, pay_amount, attendant_name):
        '''method that registers or adds a user to the database'''
        query = """INSERT INTO salerecords(product_name, quantity, pay_amount, attendant_name) 
                    VALUES (%s, %s, %s, %s)"""      
        dbcon.cursor.execute(query, (product_name, quantity, pay_amount, attendant_name))
        return  "You have made a sale record of {}".format(product_name)
