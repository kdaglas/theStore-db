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
