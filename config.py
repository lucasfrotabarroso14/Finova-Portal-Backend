from utils.global_methods import generate_secret_key

DEBUG=True

USERNAME = 'root'
PASSWORD = 'usha8tkgc'
SERVER = 'localhost'
DB = 'investment'


#string de conexao:
SQLALCHEMY_DATABASE_URI = f'mysql://{USERNAME}:{PASSWORD}@{SERVER}/{DB}'
#para quando alterar a migrate, alterar automaticamente o banco de dados:
SQLALCHEMY_TRACK_MODIFICATIONS =True

SECRET_KEY = generate_secret_key()