from flask_restx import Resource,Namespace
from services import ativos_service
from flask import request

from utils.responses import DefaultResponse

ativos_swagger = Namespace('ativos', description='Endpoints para ativos')
@ativos_swagger.route('/')
class AtivosList(Resource):
    def get(self):
        data = ativos_service.get_all()
        if data:
            result_data, status_data = data
            response = DefaultResponse(status_code=status_data, status=True, message="Busca realizada com sucesso",
                                      result=result_data)
            return response.to_json()

    def post(self):
        data = request.get_json()
        ativo_name = data.get("ativo_name")
        ativo_symbol = data.get("ativo_symbol")
        ativo_tipo = data.get("ativo_tipo")

        if not ativo_tipo or not ativo_symbol or not ativo_name:
            response = DefaultResponse(status_code=400, status=False, message='Dados incompletos',
                                       result='')
            return response.to_json()
            # return {
            #     "message": "Credenciais incompletas, preencha todos os campos"
            # }
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
            response = DefaultResponse(status_code=status, status = True,message="Busca realizda com sucesso", result=data)
            return response.to_json()


        else:
            response = DefaultResponse(status_code=status, status=False, message="Erro na busca de dados", result=data)
            return response.to_json()



    def delete(self, id):
        data, status = ativos_service.delete(id)
        if status:
            response = DefaultResponse(status_code=status, status=True, message='Task excluida com suceso',
                                       result=None)
            return response.to_json()
            # return {
            #     "status": True,
            #     "message":"Sucesso",
            #     "result": data
            # }
        else:
            response = DefaultResponse(status_code=status, status=False, message="Erro na exclusão do objeto",
                                       result=data)
            return response.to_json()

            # return {
            #     "status":False,
            #     "message": "Sucesso",
            #     "result": data
            # }

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
            response = DefaultResponse(status_code=status, status=True, message='Task atualizada com suceso',
                                       result=result)
            return response.to_json()

            # return {
            #     "status": True,
            #     "message":"Sucesso na requisição",
            #     "result" : result
            # }

        else:
            response = DefaultResponse(status_code=status, status=False, message='Dados inválidos',
                                       result=result)
            return response.to_json()
            # return {
            #     "status": False,
            #     "Message": "falha na requisição",
            #     "result": result
            # }

