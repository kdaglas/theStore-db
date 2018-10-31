''' These are the imports for the required packages '''
from storeapp.database.dbconnector import DatabaseConnection
from storeapp.database.dbprdtqueries import DatabaseQueries
import psycopg2
from storeapp import app
from storeapp.validation import Validator
from flask_jwt_extended import create_access_token, jwt_required
from flask import request, jsonify, json
from storeapp.models.product_model import Product


@app.route('/api/v2/products', methods=['POST'])
def add_product():

    ''' Function adding a product through POST method by taking in
        the input from the store owner and storing it in the database '''
    try:
        pdt_info = request.get_json()
        product_name = pdt_info.get("product_name")
        unit_price = pdt_info.get("unit_price")
        quantity = pdt_info.get("quantity")
        category = pdt_info.get("category")

        valid = Validator.validate_product_inputs(product_name, unit_price, quantity, category)

        if valid == True:
            '''checking for similar data'''
            same_name = DatabaseQueries().get_product_by_name(product_name)
            if same_name:
                return jsonify({"message":"Product already exists, just update the quantity"}), 400
            '''Add the product'''
            obj = Product(product_name, unit_price, quantity, category)
            result = obj.add_product()
            return jsonify({"message": result}), 200
        else:
            return jsonify({"message":valid}), 400
    except:
        return jsonify({"Error": "Some fields are missing, please check"}), 400
