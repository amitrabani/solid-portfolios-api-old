from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from database import DB
from security_resource import SecurityResource
from portfolio_resource import PortfolioResource
app = Flask(__name__)
cors = CORS(app, resources={r"*": {"origins": "*"}})
api = Api(app)
api.add_resource(SecurityResource, '/security')
api.add_resource(PortfolioResource, '/portfolio')

if __name__ == '__main__':
    DB.init()
    app.run(port=5000, debug=True)


