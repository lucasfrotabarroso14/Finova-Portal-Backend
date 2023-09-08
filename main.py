from flask_restful import Api
from flask import Flask
from flask_jwt_extended import JWTManager

from utils.email import enviar_email
# from utils.finance import  teste_preco


from views.ativos_views import AtivosList, AtivosDetails
from views.login import LoginList
from views.portfolios_views import PortfoliosList, PortfoliosDetails
from views.user_views import UserList, UserDetails, UsersPortfoliosDetails
from utils.global_methods import execute_query, generate_secret_key
from utils.finance import Ativo

app = Flask(__name__)

# Dados de conexão
api = Api(app)

stock = Ativo('ALUP11.SA')
print('---------------------------------------------------------------')
stock.get_stock_name()
stock.get_current_price()
stock.get_dividend_rate()

# print('---------------------------------------------------------------')




api.add_resource(UserList, "/users")
api.add_resource(UserDetails, "/users/<int:id>")


api.add_resource(AtivosList, "/ativos")
api.add_resource(AtivosDetails, "/ativos/<int:id>")


api.add_resource(PortfoliosList, "/portfolio")
api.add_resource(PortfoliosDetails, "/portfolio/<int:id>")

api.add_resource(UsersPortfoliosDetails,"/users/portfolio/<int:id>")


api.add_resource(LoginList, "/login")




app.config.from_object('config')

jwt = JWTManager(app)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port="3031")
