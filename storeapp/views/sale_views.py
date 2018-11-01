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
sale_dbquery = DatabaseQueries()

@app.route('/api/v2/sales/<productId>', methods=['POST'])
def create_sale_record(productId):

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

        

        
            pass
            '''making checks to the database'''
            
            



            # obj = Product(product_name, unit_price, quantity, category)
            # result = obj.add_product()
            # return jsonify({"message": result}), 200
            pass
        else:
            return jsonify({"message":valid}), 400
    except:
        return jsonify({"Error": "Some fields are missing, please check"}), 400


# @app.route('/api/v2/products', methods=['GET'])
# def fetch_all_products():

#     ''' Function that gets all the added products through GET method from the database '''
#     all_products = dbquery.fetch_all_products()
#     if not all_products:
#         return jsonify({"message": "No products added yet"}), 404 
#     return jsonify({'All_products': all_products,
#                     'message': 'All products have been viewed'}), 200


# @app.route('/api/v2/products/<productId>', methods=['GET'])
# def fetch_one_product(productId):

#     ''' Function that gets one the added products through GET method from the database '''
#     valid = Validator.validate_input_type(productId)

#     if valid:
#         return jsonify({"message":valid}), 400
#     product = dbquery.fetch_one_product(productId)
#     if not product:
#         return jsonify({"message": "No product with that id"}), 404 
#     return jsonify({'Product': product,
#                     'message': 'Product has been viewed'}), 200


# @app.route('/api/v2/products/<productId>', methods=['DELETE'])
# def delete_a_product(productId):

#     ''' Function that deletes an added product through DELETE method from the database '''
#     valid = Validator.validate_input_type(productId)

#     if valid:
#         return jsonify({"message":valid}), 400
#     deleted = dbquery.delete_one_product(productId)
#     if not deleted:
#         return jsonify({"message": "No products with that id"}), 404 
#     return jsonify({'message': "Successfully deleted product"}), 200


# @app.route('/api/v2/products/<productId>', methods=['PUT'])
# def update_a_product(productId):

#     '''Function for updating the quantity or price of a product '''
#     pdt_info = request.get_json()
#     unit_price = pdt_info.get("unit_price")
#     quantity = pdt_info.get("quantity")

#     updated = dbquery.update_one_product(productId, unit_price, quantity)
#     if updated:
#         print('success')
#         return jsonify({'message': 'Product has been updated'}), 200
#     return jsonify({'message': 'Product could not be updated'}), 400
