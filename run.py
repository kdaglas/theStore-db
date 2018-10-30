from storeapp import app
from storeapp.database.dbconnector import DatabaseConnection


if __name__== "__main__":
    DatabaseConnection().create_tables()
    app.run(debug=True)
    