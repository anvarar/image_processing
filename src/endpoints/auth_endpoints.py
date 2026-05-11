from src.actions.auth_action import AuthAction
from src.data.auth_data import UserData
from src.db.db_config import SessionLocal
from src.endpoints import auth_ns
from flask_restx import Resource
from flask import request
from flask import jsonify

from src.utils.jwt_handler import TokenService
from src.utils.security import PasswordService


@auth_ns.route("/signup", methods=["POST"])
@auth_ns.route("/login", methods=["GET"])
class AuthEndpoint(Resource):
    def post(self):
        data = request.get_json()
        with SessionLocal() as session:
            task_repo = UserData(session)
            password_service = PasswordService()
            token_service = TokenService()
            auth_action = AuthAction(task_repo=task_repo, password_service=password_service,
                                     token_service=token_service)

            result = auth_action.signup(data['username'], data['password'])
            return jsonify(result), 201

    def get(self):
        data = request.get_json()
        result = AuthAction.login(data['email'], data['password'])
        return jsonify(result), 200
