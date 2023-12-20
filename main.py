from flask_cors import CORS
from flask_restx import Api
from flask import Flask
from flask_jwt_extended import JWTManager
from views.ativos_views import AtivosList, AtivosDetails, ativos_swagger
from views.login import LoginList, login_swagger
from views.portfolios_views import PortfoliosList, PortfoliosDetails, portfolios_swagger
from views.user_views import UserList, UserDetails, UsersPortfoliosDetails,  users_swagger

app = Flask(__name__)

SWAGGER_URL = '/swagger'
API_URL = '/swagger.json'
api = Api(app, version='1.0', title='Documentação API Finova', description='API para o aplicativo Finova', doc=SWAGGER_URL)

api.authorizations = {
    'Bearer Auth': {
        'type': 'apiKey',
        'in': 'header',
        'name': 'Authorization'
    }
}

# Rotas de users
api.add_resource(UserList, "/users")
api.add_resource(UserDetails, "/users/<int:id>")

# Rotas de ativos(por enquanto inútil)
api.add_resource(AtivosList, "/ativos")
api.add_resource(AtivosDetails, "/ativos/<int:id>")
api.add_namespace(ativos_swagger)
# rotas do portfolio
api.add_resource(PortfoliosList, "/portfolio")
api.add_resource(PortfoliosDetails, "/portfolio/<int:id>")
api.add_namespace(portfolios_swagger)
#rota para pegar todos os portfolios de um usuario x e o swagger
api.add_resource(UsersPortfoliosDetails,"/users/portfolio/<int:id>")
api.add_namespace(users_swagger)

api.add_resource(LoginList, "/login")
api.add_namespace(login_swagger)


CORS(app, resources={r"/*": {"origins": "*"}})

app.config.from_object('config')

jwt = JWTManager(app)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port="3031")
