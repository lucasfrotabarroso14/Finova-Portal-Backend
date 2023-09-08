from utils.global_methods import execute_query


def get_all():
    query = """
    SELECT
    *
    FROM
    investment.Ativos
    """
    result, status = execute_query(query, {})

    if status:
        return result, 200
    else:
        return [], 404

def registrar_ativo(ativo_obj):
    query = """
        SELECT 
            MAX(ativo_id)
         FROM
         investment.Ativos
            
    """
    result, status = execute_query(query, {})

    if not status:
        return {
                   "status": False,
                   "result": result
               }, 500

    query ="""
    INSERT INTO 
        investment.Ativos
            (ativo_name, ativo_symbol, ativo_tipo)
                VALUES
            (%s, %s, %s)
    """

    params = (
        ativo_obj["ativo_name"],
        ativo_obj["ativo_symbol"],
        ativo_obj["ativo_tipo"]
    )
    result, status = execute_query(query, params)

    if status:
        return {
            status : True,
            "message": "Criado com sucesso"
        }, 200
    else:
        return status, 404


def get_by_id(id):
    query = """
        SELECT
            *
         FROM
        investment.Ativos
        WHERE
        ativo_id = %(id)s
            """
    params = {"id": id}
    result, status = execute_query(query, params)

    if status:
        return result, status
    else:
        return status, 404

def delete(id):
    query = """
     DELETE 
     FROM 
     investment.Ativos
     WHERE 
     ativo_id = %(id)s
     """
    params = {"id": id}
    result, status = execute_query(query, params)

    if status:
        return {"message": "Deletado com sucesso"}, status
    else:
        return {"message": "Erro ao deletar"}, status

def update(id, object):
        query = """
        UPDATE 
          investment.Ativos
        SET
            ativo_name = %s,
            ativo_symbol = %s,
            ativo_tipo = %s
        WHERE
            ativo_id = %s
        """
        params = (
            object["ativo_name"],
            object["ativo_symbol"],
            object["ativo_tipo"],
            id
        )
        result, status = execute_query(query, params)
        if status :
            return {
                status: True,
                "message": "Atualizado com sucesso"
            }, 200
        else:
            return status, 404



