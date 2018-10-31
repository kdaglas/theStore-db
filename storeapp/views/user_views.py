''' These are the imports for the required packages '''
from storeapp.database.dbconnector import DatabaseConnection
from storeapp.database.dbuserqueries import DatabaseQueries
from storeapp import app
from storeapp.validation import Validator
from flask_jwt_extended import create_access_token, jwt_required
from flask import request, jsonify, json
from storeapp.models.user_model import Attendant
import datetime


@app.route("/api/v2/auth/login", methods=['POST'])
def login():
    
    ''' This is to login the user(store owner or attenadnt) and
        if that user doesnot exist, then it returns 404 '''
    reg_info = request.get_json()

    if 'attendant_name' not in reg_info:
        return jsonify({"message": "Invalid field for username"}), 401
    elif 'password' not in reg_info:
        return jsonify({"message": "Invalid field for password"}), 401

    attendant_name = reg_info.get('attendant_name')
    password = reg_info.get('password')

    same_data = DatabaseQueries().authenticate_attendant(attendant_name, password)
    if not same_data:
        return jsonify({"message": "Invalid username or password"}), 401
    logged_in = DatabaseQueries().get_attendant_by_name(attendant_name)
    '''Creating an access token'''
    expires = datetime.timedelta(days=1)
    access_token = create_access_token(identity=logged_in['attendant_name'], expires_delta=expires)
    return jsonify({"message": "You have been logged in",
                    "token": access_token}), 200


@app.route("/api/v2/auth/signup", methods=['POST'])
# @jwt_required
def add_attendant():

    ''' Function adds an attendant through POST method by taking in
        the input from the store owner and storing it in the database '''
    try:
        reg_info = request.get_json()
        attendant_name = reg_info.get("attendant_name")
        contact = reg_info.get("contact")
        password = reg_info.get("password")
        role = "attendant"

        valid = Validator.validate_store_user_credentials(attendant_name, contact, password, role)

        if valid == True:
            '''Validating and checking for similar data'''
            same_name = DatabaseQueries().get_attendant_by_name(attendant_name)
            if same_name:
                return jsonify({"message":"Attendant name already exists, use another"}), 400
            same_contact = DatabaseQueries().get_attendant_by_contact(contact)
            if same_contact:
                return jsonify({"message":"Contact already exists, use another"}), 400
            '''Register the customer'''
            obj = Attendant(attendant_name, contact, password, role)
            result = obj.add_attendant()
            return jsonify({"message": result}), 200
        else:
            return jsonify({"message":valid}), 400
    except:
        return jsonify({"Error": "Some fields are missing, please check"}), 400


@app.route("/api/v2/auth/signup/<attendantId>", methods=["PUT"])
@jwt_required
def make_attendant_admin(attendantId):
    
    ''' This function uses the PUT method to update the role of the attendant with
        that given attendantId. it takes in an attendant id and searches for that attendant
        with that id and then returns an attendant who is now admin '''
    reg_info = request.get_json()
    role = reg_info.get('role')

    DatabaseQueries().promote_to_admin(attendantId, role)
    return jsonify({'message': 'Attendant is now admin'}), 200
    