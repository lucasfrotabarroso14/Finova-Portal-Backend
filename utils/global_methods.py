import json
import secrets
import mysql.connector
from passlib.handlers.pbkdf2 import pbkdf2_sha256


def execute_query(query, params):
    USERNAME = 'root'
    PASSWORD = 'usha8tkgc'
    SERVER = 'localhost'
    DB = 'Investment'

    try:
        connection = mysql.connector.connect(
            host=SERVER,
            user=USERNAME,
            password=PASSWORD,
            database=DB
        )
        cursor = connection.cursor()
        formatted_query = query.strip().replace("\n", "")

        if formatted_query.split(' ')[0] == "SELECT":
           cursor.execute(formatted_query, params)
           results = cursor.fetchall()

           column_names = [desc[0] for desc in cursor.description]

           data = []
           for row in results:
               data.append(dict(zip(column_names,row)))
           cursor.close()
           connection.close()
           return data, True


        else:
            cursor.execute(formatted_query, params)
            result = cursor.rowcount
            connection.commit()
        cursor.close()
        connection.close()

        print("query executada com sucesso!")
        return result, True


    except mysql.connector.Error as err:
        return str(err), False

def serialize_date(result,campo):
    string = str(campo)
    for row in result:
        row[string] = row[string].strftime('%Y-%m-%d')

def encrypt_password(senha):
    encrypted_password = pbkdf2_sha256.hash(senha)
    return encrypted_password

def decrypt_password(senha, hashed_password):
    return pbkdf2_sha256.verify(senha, hashed_password)

def generate_secret_key():
    key_size = 32
    secret_key = secrets.token_hex(key_size)
    return secret_key




