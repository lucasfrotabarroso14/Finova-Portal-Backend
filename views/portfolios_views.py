from flask_restful import Resource
from services import ativos_service, portfolios_service
from flask import request


class PortfoliosList(Resource):
    def get(self):
        data, status = portfolios_service.get_all()
        if status:
            return {
                "status":True,
                "result":data
            }
        # else:

    def post(self):
        data = request.get_json()
        user_id = data.get("user_id")
        quantidade = data.get("quantidade")
        symbol = data.get("symbol")


        if not user_id  or not quantidade :
            return {
                "message": "Credenciais incompletas, preencha todos os campos"
            }

        obj = {
            "user_id": user_id,
            "quantidade":quantidade,
            "symbol": symbol

        }
        result, status = portfolios_service.adicionar_portfolio(obj)
        return {
            "status": True,
            "message":"Sucesso na requisição",
            "result": result
        }

class PortfoliosDetails(Resource):

    def get(self, id):
        data, status = portfolios_service.get_by_id(id)
        if status:
            return {
                "status": True,
                "message":"Sucesso na requisição",
                "result": data
            }
        else:
            return {
                "status": False,
                "message": "Falha na requisição",
                "result": data
            }


    def delete(self, id):
        data, status = portfolios_service.delete(id)
        if status:
            return {
                "status":True,
                "message":"Sucesso na requisição",
                "result": data
            }
        else:
            return {
                "status": False,
                "message": "Sucesso",
                "result": data
            }
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
        if status :
            return {
                "status": True,
                "message":"Sucesso na requisição",
                "result": result
            }
        else:
            return {
                "status": False,
                "message": "Falha na requisição",
                "result": result
            }
