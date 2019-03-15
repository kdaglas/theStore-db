from flask import Flask
from flask_jwt_extended import JWTManager
import datetime
from flask import jsonify
from flask_cors import CORS


app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'my-secret'
app.config['JWT_ACCESS_TOKEN EXPIRES'] = datetime.timedelta(days=1)
jwt = JWTManager(app)
CORS(app)

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

from storeapp.views import user_views, product_views, sale_views