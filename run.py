from storeapp import app
from storeapp.database.dbuserqueries import UserDatabaseQueries
from storeapp.database.dbconnector import DatabaseConnection


dbquery = UserDatabaseQueries()
dbcreate = DatabaseConnection()

if __name__== "__main__":
    dbcreate.create_tables()
    app.run(debug=True)
    