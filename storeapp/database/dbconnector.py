import psycopg2
from storeapp import app
import psycopg2.extras as dictionary
import os


class DatabaseConnection():

    def __init__(self):

        '''This constructor creates a connection to the database depending on the configuration
            meaning if its a testing environment, then a test database is used where as if its a development
            environment then a development database is created'''
        try:
            if os.getenv('APP_SETTINGS') == "testing":
                databasename = 'testdatabase'
            else:
                databasename = 'd4k4mlq2ci52ug'
            self.dbconnection = psycopg2.connect(database=databasename, user="ircwcswofnokuh",
                                                password="1015698190d57b0d9e383a761c02e666356f9254232f15cddb12ee58cbe38c8e", host="ec2-54-225-115-234.compute-1.amazonaws.com",
                                                port="5432"
                                                )
            self.dbconnection.autocommit = True
            self.cursor = self.dbconnection.cursor(cursor_factory = dictionary.RealDictCursor)
            
        except(Exception, psycopg2.DatabaseError) as e:
            print('Cannot connect to the database {}'.format(e))

    
    def create_tables(self):

        '''This function creates the tables'''
        try:
            queries = (
                """
                CREATE TABLE IF NOT EXISTS attendants (
                    attendantId SERIAL PRIMARY KEY NOT NULL,
                    attendant_name VARCHAR NOT NULL,
                    contact VARCHAR NOT NULL,
                    password VARCHAR NOT NULL,
                    role VARCHAR NOT NULL
                );
                """,
                """
                CREATE TABLE IF NOT EXISTS products (
                    productId SERIAL PRIMARY KEY NOT NULL,
                    product_name VARCHAR NOT NULL,
                    unit_price INTEGER NOT NULL,
                    quantity INTEGER NOT NULL,
                    category VARCHAR NOT NULL
                )
                """,
                """
                CREATE TABLE IF NOT EXISTS salerecords (
                    saleId SERIAL PRIMARY KEY NOT NULL,
                    attendant_name VARCHAR NOT NULL,
                    product_name VARCHAR NOT NULL,
                    quantity INTEGER NOT NULL,
                    pay_amount VARCHAR NOT NULL,
                    today TEXT NOT NULL DEFAULT TO_CHAR(CURRENT_TIMESTAMP, 'HH:MI:SS YYYY-MM-DD')
                )
                """
            )
            for query in queries:
                self.cursor.execute(query)
        except(Exception, psycopg2.DatabaseError) as e:
            print('Cannot connect to the database {}'.format(e))


    def delete_tables(self):

        '''This function deletes the tables after usage'''
        delete_queries = (
            """DROP TABLE IF EXISTS attendants CASCADE""",
            """DROP TABLE IF EXISTS products CASCADE""",
            """DROP TABLE IF EXISTS salerecords CASCADE"""
        )
        for query in delete_queries:
            self.cursor.execute(query)     


    def closedb(self):

        '''method to close db connection'''
        self.dbconnection.close()
