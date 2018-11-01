''' These are the imports for the required packages '''
from storeapp.database.dbconnector import DatabaseConnection
from storeapp.database.dbsalequeries import DatabaseQueries
from storeapp.database.dbprdtqueries import DatabaseQueries
import psycopg2
from storeapp import app
from storeapp.validation import Validator
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from flask import request, jsonify, json
from storeapp.models.sale_model import SaleRecord

product_dbquery = DatabaseQueries()
sale_dbquery = SaleDatabaseQueries()

@app.route('/api/v2/sales', methods=['POST'])
def create_sale_record():

    ''' Function for creating a sale record through POST method 
        and storing it in the database '''
    try:
        sale_info = request.get_json()
        productId = sale_info.get("productId")
        quantity = sale_info.get("quantity")

        valid = Validator.validate_sale_record_inputs(productId, quantity)
        if valid == True:
            '''checking for the product in product table'''
            existing_product = product_dbquery.fetch_one_product(productId)
            if not existing_product:
                return jsonify({"Product selected doesnot exist, choose another"}), 400
            added_sale = sale_dbquery.create_sales_record()

        else:
            return jsonify({"message":valid}), 400
    except:
        return jsonify({"Error": "Some fields are missing, please check"}), 400


@app.route('/api/v2/sales', methods=['GET'])
def fetch_all_sale_records():

    ''' Function that gets all the created sale records through GET method from the database '''
    all_sale_records = sale_dbquery.fetch_all_sale_records()
    if not all_sale_records:
        return jsonify({"message": "No sale recorded created yet"}), 404 
    return jsonify({'sale_records': all_sale_records,
                    'message': 'All products have been viewed'}), 200


@app.route('/api/v2/sales/<saleId>', methods=['GET'])
def fetch_one_sale(saleId):

    ''' Function that gets one created sale record through GET method from the database '''
    valid = Validator.validate_input_type(saleId)

    if valid:
        return jsonify({"message":valid}), 400
    sale_record = sale_dbquery.fetch_one_sale_record(saleId)
    if not sale_record:
        return jsonify({"message": "No product with that id"}), 404 
    return jsonify({'sale_record': sale_record,
                    'message': 'Sale record has been viewed'}), 200
