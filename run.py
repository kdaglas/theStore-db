from storeapp import app
from storeapp.database.dbconnector import DatabaseConnection
from storeapp.database.dbuserqueries import UserDatabaseQueries


dbquery = UserDatabaseQueries()

if __name__== "__main__":
    DatabaseConnection().create_tables()
    dbquery.add_admin()
    app.run(debug=True)
    
