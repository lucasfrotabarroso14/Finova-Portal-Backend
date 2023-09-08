from datetime import timedelta
from flask_restful import Resource
from flask import request, jsonify, make_response
import requests
from flask_jwt_extended import create_access_token
from utils.global_methods import decrypt_password

from services.user_service import get_by_email


class LoginList(Resource):
    def post(self):
        data = request.get_json()
        email = data.get("email")
        password = data.get("password")

        if not email or not password:
            return {
                "message": "Credenciais incompletas, preencha todos os campos"
            }
        result, status = get_by_email(email)
        if status:
            user = result[0]
            hashed_password = user["password"]
            if decrypt_password(password, hashed_password):
                access_token = create_access_token(
                    identity=user["user_id"],
                    expires_delta=timedelta(days=1)
                )
                return {
                    'access_token':access_token,
                    'message':'Login realizado com sucesso',
                    'status':True
                }, 200
                return {
                    "message": "Credenciais incorretas, tente novamente."
                }

            else:
                return {
                    "message":"Credenciais incorretas, tente novamente."
                }

