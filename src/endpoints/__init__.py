from flask import Blueprint
from flask_restx import Api

from src.endpoints.namespaces import auth_ns

api_blueprint = Blueprint("api", __name__)
api = Api(api_blueprint)
api.add_namespace(auth_ns)
