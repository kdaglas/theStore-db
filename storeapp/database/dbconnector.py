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
                user = 'postgres'
                password = 'admin'
                host = 'localhost'
            else:
                # databasename = 'thestoredb'
                # user = 'postgres'
                # password = 'admin'
                # host = 'localhost'
                databasename = 'd7gvg3da3mefg9'
                user = 'uxduccjuifcnng'
                password = 'f3569e7d3c9c85212475fc95faa5ad24bee04501290a1ba8413075435a5ea878'
                host = 'ec2-75-101-133-29.compute-1.amazonaws.com'
                
            self.dbconnection = psycopg2.connect(database=databasename,
                                                user=user,
                                                password=password,
                                                host=host,
                                                port="5432"
                                                )

            self.dbconnection.autocommit = True
            self.cursor = self.dbconnection.cursor(cursor_factory = dictionary.RealDictCursor)
            # self.create_tables()
            self.delete_admin()
            self.add_admin()
            self.delete_product()
            self.add_product()

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
                print('creating tables')
                self.cursor.execute(query)
        except(Exception, psycopg2.DatabaseError) as e:
            print('Cannot connect to the database {}'.format(e))


    def delete_product(self):
        '''deletes an admin'''
        query = """DELETE FROM products WHERE product_name = %s"""
        self.cursor.execute(query, ('baby powder',))


    def delete_admin(self):
        '''deletes an admin'''
        query = """DELETE FROM attendants WHERE attendant_name = %s"""
        self.cursor.execute(query, ('admin',))


    def add_admin(self):
        '''registers an admin'''
        query = """INSERT INTO attendants(attendant_name, contact, password, role) 
                    VALUES (%s, %s, %s, %s)"""      
        self.cursor.execute(query, ('admin', '+256-700-000000', 'Admin17', 'admin'))


    def add_product(self):
        '''registers an admin'''
        query = """INSERT INTO products(product_name, unit_price, quantity, category) 
                    VALUES (%s, %s, %s, %s)"""      
        self.cursor.execute(query, ('baby powder', '1500', '180', 'babies'))


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
