''' These are the imports for the required packages '''
from storeapp.database.dbconnector import DatabaseConnection
from storeapp.database.dbuserqueries import UserDatabaseQueries
from storeapp import app
from storeapp.validation import Validator
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from flask import request, jsonify, json
from storeapp.models.user_model import Attendant
import datetime
from datetime import timedelta


dbquery = UserDatabaseQueries()

@app.route("/api/v2/auth/login", methods=['POST'])
def login():
    ''' login the user(attendant)
        and if that user doesnot exist,
        then it returns 404 '''
    try:
        reg_info = request.get_json()
        attendant_name = reg_info.get("attendant_name")
        password = reg_info.get("password")

        '''checking for right keys in json'''
        if not reg_info.get("attendant_name") or not reg_info.get("password"):
            return jsonify({"Error": "Some fields are missing, please check"}), 400

        '''checking if the user exists in the db'''
        same_data = dbquery.authenticate_attendant(attendant_name, password)
        if not same_data:
            return jsonify({"message": "Invalid username or password"}), 401

        '''logging in the user'''
        logged_in = dbquery.get_attendant_by_name(attendant_name)
        expires = datetime.timedelta(days=1)
        access_token = create_access_token(identity=logged_in['attendant_name'], expires_delta=expires)
        return jsonify({"message": "You have been logged in",
                        "token": access_token}), 200
    except:
        return jsonify({"Error": "Some fields are missing, please check"}), 400


@app.route("/api/v2/auth/signup", methods=['POST'])
@jwt_required
def add_attendant():
    ''' Function adds an attendant by the
        POST method by taking in it takes user
        input and stores it in the dp '''
    try:
        reg_info = request.get_json()
        attendant_name = reg_info.get("attendant_name")
        contact = reg_info.get("contact")
        password = reg_info.get("password")
        role = "attendant"

        '''checking for user permissions'''
        user_identity = get_jwt_identity()
        logged_in = dbquery.get_attendant_by_name(attendant_name=user_identity)
        if logged_in['role'] != 'admin':
            return jsonify({'message': "Unauthorized to operate this feature"}), 401

        '''Validating and checking for correct user data'''
        valid = Validator.validate_store_user_credentials(attendant_name, contact, password, role)
        if valid != True:
            return jsonify({"message":valid}), 400

        '''Validating and checking for similar data'''
        same_name = dbquery.get_attendant_by_name(attendant_name)
        if same_name:
            return jsonify({"message":"Attendant name already exists, use another"}), 400
        same_contact = dbquery.get_attendant_by_contact(contact)
        if same_contact:
            return jsonify({"message":"Contact already exists, use another"}), 400

        '''Register the customer'''
        obj = Attendant(attendant_name, contact, password, role)
        result = obj.add_attendant()
        return jsonify({"message": result}), 201
    except:
        return jsonify({"Error": "Some fields are missing, please check"}), 400


@app.route('/api/v2/auth/signup', methods=['GET'])
@jwt_required
def fetch_all_attendants():
    ''' getting all the added attendants through
        GET method from the database '''

    '''checking for user permissions'''
    user_identity = get_jwt_identity()
    logged_in = dbquery.get_attendant_by_name(attendant_name=user_identity)
    if logged_in['role'] != 'admin':
        return jsonify({'message': "Unauthorized to operate this feature"}), 401

    '''getting all users'''
    all_attendants = dbquery.fetch_all_attendants()
    if not all_attendants:
        return jsonify({"message": "No attendants added yet"}), 404 
    return jsonify({'All_attendants': all_attendants,
                    'message': 'All attendants have been viewed'}), 200


@app.route('/api/v2/auth/signup/<attendantId>', methods=['GET'])
@jwt_required
def fetch_attendant(attendantId):
    ''' Fetching one attendant
        using GET method from the database '''

    '''Validating and checking for input type'''
    valid = Validator.validate_input_type(attendantId)
    if valid:
        return jsonify({"message":valid}), 400

    '''checking for user permissions'''
    user_identity = get_jwt_identity()
    logged_in = dbquery.get_attendant_by_name(attendant_name=user_identity)
    if logged_in['role'] != 'admin':
        return jsonify({'message': "Unauthorized to operate this feature"}), 401

    '''fetching one attendant'''
    attendant = dbquery.fetch_one_attendant(attendantId)
    if not attendant:
        return jsonify({"message": "No attendant with that id"}), 404 
    return jsonify({'Attendant': attendant,
                    'message': 'Attendant has been viewed'}), 200


@app.route("/api/v2/auth/signup/<attendantId>", methods=["PUT"])
@jwt_required
def make_attendant_admin(attendantId):
    ''' uses the PUT method to update the role of the
        attendant with that given attendantId. '''
    try:
        reg_info = request.get_json()
        role = reg_info.get("role")

        '''Validating and checking for input type'''
        valid = Validator.validate_input_type(attendantId)
        if valid:
            return jsonify({"message":valid}), 400

        '''checking for user permissions'''
        user_identity = get_jwt_identity()
        logged_in = dbquery.get_attendant_by_name(attendant_name=user_identity)
        if logged_in['role'] != 'admin':
            return jsonify({'message': "Unauthorized to operate this feature"}), 401

        '''checking for right keys in json'''
        if not reg_info.get("role"):
            return jsonify({"Error": "Some fields are missing, please check"}), 400

        '''Validating and checking for correct user data'''
        valid = Validator.validate_role(role)
        if valid != True:
            return jsonify({"message":valid}), 400
        
        '''update the role of the user'''
        promoted = dbquery.promote_to_admin(attendantId, role)
        if not promoted:
            return jsonify({"message": "No attendant with that id"}), 404 
        return jsonify({'message': 'Attendant role has been updated'}), 200
    except:
        return jsonify({"Error": "Some fields are missing, please check"}), 400
    

@app.route('/api/v2/auth/signup/<attendantId>', methods=['DELETE'])
@jwt_required
def delete_attendant(attendantId):
    ''' deletes a user through DELETE 
        method from the database '''
    
    '''Validating and checking for input type'''
    valid = Validator.validate_input_type(attendantId)
    if valid:
        return jsonify({"message":valid}), 400

    '''checking for user permissions'''
    user_identity = get_jwt_identity()
    logged_in = dbquery.get_attendant_by_name(attendant_name=user_identity)
    if logged_in['role'] != 'admin':
        return jsonify({'message': "Unauthorized to operate this feature"}), 401

    deleted = dbquery.delete_user(attendantId)
    if not deleted:
        return jsonify({"message": "No attendant with that id"}), 404 
    return jsonify({'message': "Successfully deleted attendant"}), 200
