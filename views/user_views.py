from flask_restx import Resource, Namespace


from services import user_service
from flask import request,make_response,jsonify
import json
from utils.global_methods import encrypt_password, serialize_date

users_swagger = Namespace('users', description='Endpoints de user')
@users_swagger.route('/')
class UserList(Resource):
    def get(self):
        data = user_service.get_all()
        if data:
            result_data, status_data = data
            if status_data == 200:
                result_data = {
                    "status": True,
                    "message": "Sucesso na requisição",
                    "result": result_data
                }
                return result_data
    def post(self):
        data = request.get_json()

        username = data.get("username")
        password = data.get("password")
        email = data.get("email")



        if not username or not password or not email:
            return {
                "message": "Credenciais incompletas, preencha todos os campos"
            }
        password = encrypt_password(password)
        user_obj = {
            "username": username,
            "password": password,
            "email": email
        }
        response = user_service.register_user(user_obj)
        return response

@users_swagger.route('/<int:id>')
class UserDetails(Resource):
    def get(id):
        data, status = user_service.get_by_id(id)
        if status :
            return {
                "status": True,
                "message": "Sucesso",
                "result" : data
            }
        else:
            return {
                "status": False,
                "message":"Falha na requisição",
                "result": data
            }
    def delete(id):
        data, status = user_service.delete(id)
        if status:
            return {
                "status": True,
                "message": "Excluido com sucesso!",
                "result": data
            }
        else:
            return {
                "status": False,
                "message": "Falha na requisição",
                "result": data
            }
@users_swagger.route('/portfolio/<int:id>')
class UsersPortfoliosDetails(Resource):
    def get(self,id):
        data, status = user_service.get_users_portfolios(id)
        if status:
            return {
                "status": True,
                "message": "Sucesso",
                "result": data
            }

        else:
            return {
                "status": False,
                "message": "Falha na requisição",
                "result": data
            }


    # def put(self, id):
    #     data = request.get_json()
    #     username = data.get("username")
    #     password = data.get("password")
    #     email = data.get("email")


