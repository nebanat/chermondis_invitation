from flask import Blueprint
from flask_restplus import Api
from api.blueprints.user.resources import User

# registers a new user blueprint
user = Blueprint('user', __name__, template_folder='templates')

user_api = Api(user)

user_api.add_resource(User, '/api/v1/user')
