from flask_restful import Resource, reqparse
from porfolio_model import PortfolioModel
import json


class PortfolioResource(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('portfolio_name',
                    type=str,
                    required=True,
                    help="no name provided."
                        )
    def get(self):
        portfolios_array = []

        for security in PortfolioModel.get_all_objects_in_db():
            security.pop('_id')
            portfolios_array.append(security)
        return {'portfolios': portfolios_array}, 200

    def post(self):
        data = self.parser.parse_args()
        data = self.parser.parse_args()
        portfolio_name = str(data['portfolio_name']).upper()
        a = PortfolioModel.find_portfolio_in_db("portfolios", {"portfolio_name": portfolio_name.upper()})
        if PortfolioModel.find_portfolio_in_db("portfolios", {"portfolio_name": portfolio_name.upper()}):
            return {'message': "A portfolio with name '{}' already exists.".format(portfolio_name.upper())}, 400
        else:
            try:
                PortfolioModel.insert_porfolio(portfolio_name)
            except:
                return {"message": "An error occurred while adding the portfolio."}, 500
            return {"message": "portfolio created successfully"}, 201

    def delete(self):
        data = self.parser.parse_args()
        portfolio_name = str(data['portfolio_name'].upper())
        if not PortfolioModel.find_portfolio_in_db("portfolios", {"portfolio_name": portfolio_name.upper()}):
            return {'message': "An portfolio with name '{}' does not exists.".format(portfolio_name.upper())}, 400
        else:
            try:
                PortfolioModel.delete_portfolio(portfolio_name.upper())
            except:
                return {"message": "An error occurred while delete the portfolio."}, 500
            return {"message": "'{}' has been deleted successfully.".format(data['portfolio_name'].upper())}, 201

    # def put(self):
    #     data = self.parser.parse_args()
    #     if data['ticker'] is None or data['amount'] is None:
    #         return {'message': "you must supply a ticker and amount".format(data['ticker'].upper())}, 400
    #     if not SecurityModel.find_object_in_db("securities", {'ticker': str(data['ticker']).upper()}):
    #         return {'message': "An item with ticker '{}' does not exists.".format(data['ticker'])}, 400
    #     else:
    #         try:
    #             SecurityModel.change_securities_amount(str(data['ticker']).upper(), data['amount'])
    #         except:
    #             return {"message": "An error occurred while updating the item."}, 500
    #         return 201
    #

