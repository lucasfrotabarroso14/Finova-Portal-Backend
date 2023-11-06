from flask_restx import Resource,Namespace
from services import ativos_service
from flask import request
ativos_swagger = Namespace('ativos', description='Endpoints para ativos')
@ativos_swagger.route('/')
class AtivosList(Resource):
    def get(self):
        data = ativos_service.get_all()
        if data:
            result_data, status_data = data
            return {
                "status": True,
                "result": result_data
            }

    def post(self):
        data = request.get_json()
        ativo_name = data.get("ativo_name")
        ativo_symbol = data.get("ativo_symbol")
        ativo_tipo = data.get("ativo_tipo")

        if not ativo_tipo or not ativo_symbol or not ativo_name:
            return {
                "message": "Credenciais incompletas, preencha todos os campos"
            }
        ativo_obj = {
            "ativo_name" :ativo_name,
            "ativo_symbol" :ativo_symbol,
            "ativo_tipo" :ativo_tipo

        }
        response = ativos_service.registrar_ativo(ativo_obj)
        return response

@ativos_swagger.route('/<int:id>')
class AtivosDetails(Resource):

    def get(self,id):
        data, status = ativos_service.get_by_id(id)
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

    def delete(self, id):
        data, status = ativos_service.delete(id)
        if status:
            return {
                "status": True,
                "message":"Sucesso",
                "result": data
            }
        else:
            return {
                "status":False,
                "message": "Sucesso",
                "result": data
            }

    def put(self,id):
        data = request.get_json()
        ativo_name = data.get("ativo_name")
        ativo_symbol = data.get("ativo_symbol")
        ativo_tipo = data.get("ativo_tipo")

        obj = {
            "ativo_name":ativo_name,
            "ativo_symbol": ativo_symbol,
            "ativo_tipo": ativo_tipo
        }
        result, status = ativos_service.update(id, obj)
        if status:
            return {
                "status": True,
                "message":"Sucesso na requisição",
                "result" : result
            }

        else:
            return {
                "status": False,
                "Message": "falha na requisição",
                "result": result
            }

