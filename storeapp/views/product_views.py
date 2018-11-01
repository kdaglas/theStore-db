''' These are the imports for the required packages '''
from storeapp.database.dbconnector import DatabaseConnection
from storeapp.database.dbprdtqueries import DatabaseQueries
import psycopg2
from storeapp import app
from storeapp.validation import Validator
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from flask import request, jsonify, json
from storeapp.models.product_model import Product


dbquery = DatabaseQueries()

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
            same_name = dbquery.get_product_by_name(product_name)
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


@app.route('/api/v2/products', methods=['GET'])
def fetch_all_products():

    ''' Function that gets all the added products through GET method from the database '''
    all_products = dbquery.fetch_all_products()
    if not all_products:
        return jsonify({"message": "No products added yet"}), 404 
    return jsonify({'All_products': all_products,
                    'message': 'All products have been viewed'}), 200


@app.route('/api/v2/products/<productId>', methods=['GET'])
def fetch_one_product(productId):

    ''' Function that gets one the added products through GET method from the database '''
    valid = Validator.validate_input_type(productId)

    if valid:
        return jsonify({"message":valid}), 400
    product = dbquery.fetch_one_product(productId)
    if not product:
        return jsonify({"message": "No product with that id"}), 404 
    return jsonify({'Product': product,
                    'message': 'Product has been viewed'}), 200


@app.route('/api/v2/products/<productId>', methods=['DELETE'])
def delete_a_product(productId):

    ''' Function that deletes an added product through DELETE method from the database '''
    valid = Validator.validate_input_type(productId)

    if valid:
        return jsonify({"message":valid}), 400
    deleted = dbquery.delete_one_product(productId)
    if not deleted:
        return jsonify({"message": "No products with that id"}), 404 
    return jsonify({'message': "Successfully deleted product"}), 200


@app.route('/api/v2/products/<productId>', methods=['PUT'])
def update_a_product(productId):

    '''Function for updating the quantity or price of a product '''
    pdt_info = request.get_json()
    quantity = pdt_info.get("quantity")

    valid = Validator.validate_quantity_input(quantity)
    if valid == True:
        updated = dbquery.update_one_product(productId, quantity)
        if updated:
            print('success')
            return jsonify({'message': 'Product has been updated'}), 200
        return jsonify({'message': 'Product could not be updated'}), 400
    else:
        return jsonify({"message":valid}), 400


@app.route('/api/v2/products/price/<productId>', methods=['PUT'])
def update_product_price(productId):

    '''Function for updating the quantity or price of a product '''
    pdt_info = request.get_json()
    unit_price = pdt_info.get("unit_price")

    valid = Validator.validate_quantity_input(unit_price)
    if valid == True:
        updated = dbquery.update_one_product(productId, unit_price)
        if updated:
            print('success')
            return jsonify({'message': 'Product price has been updated'}), 200
        return jsonify({'message': 'Product could not be updated'}), 400
    else:
        return jsonify({"message":valid}), 400
