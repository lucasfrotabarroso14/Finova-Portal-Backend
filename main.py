from flask_cors import CORS
from flask_restful import Api
from flask import Flask
from flask_jwt_extended import JWTManager
from views.ativos_views import AtivosList, AtivosDetails
from views.login import LoginList
from views.portfolios_views import PortfoliosList, PortfoliosDetails
from views.user_views import UserList, UserDetails, UsersPortfoliosDetails


app = Flask(__name__)

# Dados de conexão
api = Api(app)


# Rotas de users
api.add_resource(UserList, "/users")
api.add_resource(UserDetails, "/users/<int:id>")

# Rotas de ativos(por enquanto inútil)
api.add_resource(AtivosList, "/ativos")
api.add_resource(AtivosDetails, "/ativos/<int:id>")

# rotas do portfolio
api.add_resource(PortfoliosList, "/portfolio")
api.add_resource(PortfoliosDetails, "/portfolio/<int:id>")

#rota para pegar todos os portfolios de um usuario x
api.add_resource(UsersPortfoliosDetails,"/users/portfolio/<int:id>")


api.add_resource(LoginList, "/login")


CORS(app, resources={r"/*": {"origins": "*"}})

app.config.from_object('config')

jwt = JWTManager(app)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port="3031")
