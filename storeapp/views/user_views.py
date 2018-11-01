''' These are the imports for the required packages '''
from storeapp.database.dbconnector import DatabaseConnection
from storeapp.database.dbuserqueries import UserDatabaseQueries
from storeapp import app
from storeapp.validation import Validator
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from flask import request, jsonify, json
from storeapp.models.user_model import Attendant
import datetime


dbquery = UserDatabaseQueries()

@app.route("/api/v2/auth/login", methods=['POST'])
def login():
    
    ''' This is to login the user(attenadnt) and
        if that user doesnot exist, then it returns 404 '''
    try:
        reg_info = request.get_json()
        attendant_name = reg_info.get('attendant_name')
        password = reg_info.get('password')

        same_data = dbquery.authenticate_attendant(attendant_name, password)
        if not same_data:
            return jsonify({"message": "Invalid username or password"}), 401
        logged_in = dbquery.get_attendant_by_name(attendant_name)
        '''Creating an access token'''
        expires = datetime.timedelta(days=1)
        access_token = create_access_token(identity=logged_in['attendant_name'], expires_delta=expires)
        return jsonify({"message": "You have been logged in",
                        "token": access_token}), 200
    except:
        return jsonify({"Error": "Some fields are missing, please check"}), 400


@app.route("/api/v2/auth/signup", methods=['POST'])
@jwt_required
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
            user_identity = get_jwt_identity()
            logged_in = dbquery.get_attendant_by_name(attendant_name=user_identity)
            
            if logged_in['role'] != 'admin':
                return jsonify({'message': "Unauthorized to operate this feature"})

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
    try:
        reg_info = request.get_json()
        role = reg_info.get('role')

        valid = Validator.validate_role(role)
        if valid == True:
            user_identity = get_jwt_identity()
            logged_in = dbquery.get_attendant_by_name(attendant_name=user_identity)
            
            if logged_in['role'] != 'admin':
                return jsonify({'message': "Unauthorized to operate this feature"})
            dbquery.promote_to_admin(attendantId, role)
            return jsonify({'message': 'Attendant is now admin'}), 200
        else:
            return jsonify({"message":valid}), 400
    except:
        return jsonify({"Error": "Some fields are missing, please check"}), 400
    