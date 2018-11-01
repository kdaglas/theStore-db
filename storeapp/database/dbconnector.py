import psycopg2
from storeapp import app
import psycopg2.extras as dictionary
import os


class DatabaseConnection():

    def __init__(self):

        '''This constructor creates a connection to the database depending on the configuration
            meaning if its a testing environment, then a test database is used where as if its a development
            environment then a development database is created'''
        # try:
        #     if not app.config['TESTING']:
        #         self.dbconnection = psycopg2.connect(database="thestoredb", user="postgres",
        #                                     password="admin", host="localhost",
        #                                     port="5432"
        #                                     )
        #     else:
        #         self.dbconnection = psycopg2.connect(database="testdb", user="postgres",
        #                                     password="admin", host="localhost",
        #                                     port="5432"
        #                                     )
        #     self.dbconnection.autocommit = True
        #     self.cursor = self.dbconnection.cursor(cursor_factory = dictionary.RealDictCursor)
        # except:
        #     print('Cannot connect to the database')



        try:
            if os.getenv('APP_SETTINGS') == "testing":
                dbname = 'testdb'
            else:
                dbname = 'thestoredb'
            self.dbconnection = psycopg2.connect(database=dbname, user="postgres",
                                                password="admin", host="localhost",
                                                port="5432"
                                                )

            self.dbconnection.autocommit = True
            self.cursor = self.dbconnection.cursor(cursor_factory = dictionary.RealDictCursor)
            # print(dbname)

        except(Exception, psycopg2.DatabaseError) as e:
            print('Cannot connect to the database {}'.format(e))

    
    def create_tables(self):

        '''This function creates the tables'''
        try:
            queries = (
                """
                CREATE TABLE IF NOT EXISTS admin (
                    adminId SERIAL PRIMARY KEY NOT NULL,
                    username VARCHAR NOT NULL,
                    password VARCHAR NOT NULL
                );
                """,
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
                    attendantId INTEGER NOT NULL,
                    productId INTEGER NOT NULL,
                    quantity INTEGER NOT NULL,
                    pay_amount VARCHAR NOT NULL,
                    today TEXT NOT NULL DEFAULT TO_CHAR(CURRENT_TIMESTAMP, 'HH:MI:SS YYYY-MM-DD'),
                    FOREIGN KEY (attendantId) REFERENCES attendants(attendantId) ON DELETE CASCADE ON UPDATE CASCADE,
                    FOREIGN KEY (productId) REFERENCES products(productId) ON DELETE CASCADE ON UPDATE CASCADE
                )
                """
            )
            for query in queries:
                self.cursor.execute(query)
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)


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
