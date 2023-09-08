from utils.email import enviar_email
from utils.global_methods import execute_query, serialize_date


def get_all():
    query = """ 
    SELECT
    *
    FROM
    investment.Users
    """
    result, status = execute_query(query,{})

    if status:
        return result, 200

    else:
        return [], 404

def register_user(user_obj):
    query = """
    SELECT 
        MAX(user_id)
    FROM 
        investment.Users
    """

    result, status = execute_query(query, {})
    if not status :
        return {
                   "status": False,
                   "result": result
               }, 500
    query = """
    INSERT INTO 
        investment.Users
            (username, password, email)
                VALUES
            (%s, %s, %s)
    """

    params = (
        user_obj["username"],
        user_obj["password"],
        user_obj["email"]
    )
    enviar_email(params[0], params[2])
    result, status = execute_query(query,params)


    if status:
        return {
            status: True,
            "message":"Criado com sucesso"
        }, 200
    else:
        return status, 404

def get_by_id(id):
    query = """
    SELECT 
    *
    FROM 
    investment.Users
    WHERE
    user_id = %(id)s
    """
    params = {"id": id}
    result, status = execute_query(query, params)

    if status:
        return result, status
    else:
        return [], status

def delete(id):
    query = """
        DELETE
        FROM 
        investment.Users
        WHERE
        user_id = %(id)s
        """
    params = {"id": id}
    result, status = execute_query(query, params)

    if status:
        return result, status
    else:
        return [], status

def get_by_email(email):
    query = """
       SELECT 
       *
       FROM 
       investment.Users
       WHERE
       email = %(email)s
       """
    params = {"email": email}
    result, status = execute_query(query, params)

    if status:
        return result, status
    else:
        return [], status

def get_users_portfolios(id):
    query = """
    SELECT 
    *
    FROM 
    investment.Portfolios
    WHERE
    user_id = %(id)s
    """
    params = {"id": id}
    result, status = execute_query(query, params)

    if status:
        serialize_date(result, "data_aquisicao")
        return result, 200
    else:
        return [], 404

