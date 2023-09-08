from utils.global_methods import execute_query, serialize_date
from utils.finance import Ativo
from datetime import datetime

# service
def get_all():
    query = """ 
    SELECT
    *
    FROM
    investment.Portfolios
    """
    result, status = execute_query(query, {})

    if status:
        serialize_date(result,"data_aquisicao")
        return result, 200

    else:
        return [], 404


def adicionar_portfolio(obj):
    query = """
    SELECT
        MAX(portfolio_id)
    FROM
        investment.Portfolios
    """
    result, status = execute_query(query, {})

    if not status:
        return {
            "status": False,
            "result": result
        }, 500

    query = """
    INSERT INTO 
        investment.Portfolios
          (user_id,  quantidade, data_aquisicao, custo_unitario,symbol, custo_total)
          VALUES
          (%s, %s, %s, %s, %s, %s)
    """

    Stock = Ativo(obj["symbol"])
    current_price = Stock.get_current_price()
    obj["custo_unitario"] = current_price
    obj["custo_total"] = obj["custo_unitario"] * obj["quantidade"]

    obj["data_aquisicao"]= datetime.today()
    params = (
        obj["user_id"],
        obj["quantidade"],
        obj["data_aquisicao"] ,
        obj["custo_unitario"],
        obj["symbol"],
        obj["custo_total"]

    )
    result, status = execute_query(query, params)

    if status:
        return {
                   status: True,
                   "message": "Criado com sucesso"
               }, 200
    else:
        return status, 404

def get_by_id(id):
    query ="""
    SELECT
    *
    FROM
    investment.Portfolios
    WHERE
    Portfolio_id = %(id)s
    """
    params = {"id":id}
    result, status = execute_query(query, params)


    if status:
        serialize_date(result, "data_aquisicao")
        return result, 200
    else:
        return [], 404

def delete(id):
    query = """
    DELETE FROM
        investment.Portfolios
    WHERE
        Portfolio_id = %(id)s 
    """
    params = {"id": id}
    result, status = execute_query(query, params)

    if status:
        return {"message": "Deletado com sucesso"}, status
    else:
        return {"message": "Erro ao deletar"}, status

def update(id,obj):
    query = """
    UPDATE
     investment.Portfolios
         SET
     user_id = %s,
     quantidade = %s,
     custo_total = %s
     
        WHERE   
    Portfolio_id = %s
    """


    obj["custo_total"] = obj["custo_unitario"] * obj["quantidade"]

    params = (
        obj["user_id"],
        obj["quantidade"],
        obj["custo_total"],
        id
    )
    result, status = execute_query(query, params)
    if status:
        return {"message": "Atualizado com sucesso"}, status
    else:
        return {"message": "Erro na atualização"}, status