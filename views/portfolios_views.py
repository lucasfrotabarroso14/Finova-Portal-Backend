from flask_restx import Resource,Namespace
from services import ativos_service, portfolios_service
from flask import request

from utils.responses import DefaultResponse

portfolios_swagger = Namespace('portfolios', description='Endpoints para portfolios')
@portfolios_swagger.route('/')
class PortfoliosList(Resource):
    def get(self):
        data, status = portfolios_service.get_all()
        if status:
            response = DefaultResponse(status_code=status, status=True, message="Busca realizada com sucesso",
                                       result=data)
            return response.to_json()
            # return {
            #     "status":True,
            #     "result":data
            # }
        # else:

    def post(self):
        data = request.get_json()
        user_id = data.get("user_id")
        quantidade = data.get("quantidade")
        symbol = data.get("symbol")


        if not user_id  or not quantidade :
            response = DefaultResponse(status_code=400, status=False, message='Dados incompletos',
                                       result='')
            return response.to_json()
        #     return {
        #         "message": "Credenciais incompletas, preencha todos os campos"
        #     }

        obj = {
            "user_id": user_id,
            "quantidade":quantidade,
            "symbol": symbol

        }
        result, status = portfolios_service.adicionar_portfolio(obj)
        response = DefaultResponse(status_code=status, status= True, message ='Criado com sucesso',
                                           result=result)
        return response.to_json()
        # return {
        #     "status": True,
        #     "message":"Sucesso na requisição",
        #     "result": result
        # }
@portfolios_swagger.route('/<int:id>')
class PortfoliosDetails(Resource):

    def get(self, id):
        data, status = portfolios_service.get_by_id(id)
        if status:
            response = DefaultResponse(status_code=status, status=True, message="Busca realizada com sucesso",
                                       result=data)
            return response.to_json()

            # return {
            #     "status": True,
            #     "message":"Sucesso na requisição",
            #     "result": data
            # }
        else:
            response = DefaultResponse(status_code=status, status=False, message="Erro na busca de dados", result=data)
            return response.to_json()
            # return {
            #     "status": False,
            #     "message": "Falha na requisição",
            #     "result": data
            # }


    def delete(self, id):
        data, status = portfolios_service.delete(id)
        if status:
            response = DefaultResponse(status_code=status, status=True, message='Task excluida com suceso',
                                       result=None)
            return response.to_json()
            # return {
            #     "status":True,
            #     "message":"Sucesso na requisição",
            #     "result": data
            # }
        else:
            response = DefaultResponse(status_code=status, status=False, message="Erro na exclusão do objeto",
                                       result=data)
            return response.to_json()
            # return {
            #     "status": False,
            #     "message": "Sucesso",
            #     "result": data
            # }
    def put(self, id):
        data = request.json

        get_old_data = portfolios_service.get_by_id(id)
        custo_unitario = get_old_data[0][0]["custo_unitario"]

        user_id = data.get("user_id")
        quantidade = data.get("quantidade")



        obj = {
            "user_id":user_id,
            "quantidade":quantidade,
            "custo_unitario" : custo_unitario

        }
        result, status = portfolios_service.update(id,obj)
        if status:
            response = DefaultResponse(status_code=status, status=True, message='Task atualizada com suceso',
                                       result=result)
            return response.to_json()

            # return {
            #     "status": True,
            #     "message":"Sucesso na requisição",
            #     "result": result
            # }

        else:
            response = DefaultResponse(status_code=status, status=False, message='Dados inválidos',
                                       result=result)
            return response.to_json()
            # return {
            #     "status": False,
            #     "message": "Falha na requisição",
            #     "result": result
            # }
