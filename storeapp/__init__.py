from flask import Flask
from flask_jwt_extended import JWTManager
import datetime
from flask import jsonify

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'my-secret'
app.config['JWT_ACCESS_TOKEN EXPIRES'] = datetime.timedelta(days=1)
jwt = JWTManager(app)

@app.errorhandler(404)
def page_not_found(e):

    ''' this function is for catching an error and 
        returning a message incase of an invalid url '''
    return jsonify({"message": "Please put a valid URL"}), 405


@app.errorhandler(405)
def method_not_allowed(e):

    ''' this function is for catching an error and 
        returning a message incase of a method not allowed '''
    return jsonify({"message": "Method not allowed"}), 405


@app.errorhandler(500)
def internal_server_error(e):

    ''' this function is for catching an error and 
        returning a message incase of an internal server error '''
    return jsonify({"message": "Internal server error"}), 500

from storeapp.views import user_views, product_views