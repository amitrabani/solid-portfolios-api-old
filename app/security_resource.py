from flask_restful import Resource, reqparse
from security_model import SecurityModel
from yahoo_api import get_security_details
import json

class SecurityResource(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('ticker',
                    type=str,
                    required=True,
                    help="Every security needs a ticker."
                    )
    parser.add_argument('amount',
                        type=int)
    parser.add_argument('portfolio_name',
                        type=str,
                        required=False,
                        )

    def post(self):
        data = self.parser.parse_args()
        security_ticker = str(data['ticker']).upper()
        portfolio_name =  str(data['portfolio_name']).upper()
        response = get_security_details(security_ticker.upper())
        if response.status_code == 404:
            return {'message': "An item with ticker '{}' does not exists.".format(security_ticker.upper())}, 400
        security_details = json.loads(response.text)
        if len(SecurityModel.find_one_in_array(portfolio_name, security_ticker)) >= 2:
            return {'message': "An item with ticker '{}' already exists.".format(security_ticker.upper())}, 400
        else:
            try:
                SecurityModel.insert_security(security_details, portfolio_name)
            except:
                return {"message": "An error occurred while inserting the item."}, 500
            return {"message": "Security added successfully"}, 201

    def put(self):
        data = self.parser.parse_args()
        security_ticker = str(data['ticker']).upper()
        security_amount  = (data['amount'])
        portfolio_name = str(data['portfolio_name']).upper()
        if security_ticker is None or security_amount is None or portfolio_name is None:
            return {'message': "you must supply a ticker, amount and portfolio name".format(data['ticker'].upper())}, 400
        if len(SecurityModel.find_one_in_array(portfolio_name, security_ticker)) <= 1:
            return {'message': "An item with ticker '{}' does not exists.".format(security_ticker.upper())}, 400
        else:
            try:
                SecurityModel.change_securities_amount(portfolio_name, security_ticker, security_amount)
            except:
                return {"message": "An error occurred while updating the item."}, 500
            return 201

    def get(self):
        securities_array = []
        for security in SecurityModel.get_all_objects_in_db():
            securities_array.append(security)
        return {'securities': str(securities_array)}, 200

    def delete(self):
        data = self.parser.parse_args()
        security_ticker = str(data['ticker'].upper())
        portfolio_name = str(data['portfolio_name']).upper()
        if security_ticker == "NONE" or portfolio_name == "NONE":
            return {'message': "you must supply a ticker and portfolio name"}, 400
        if len(SecurityModel.find_one_in_array(portfolio_name, security_ticker)) >= 2:
            try:
                SecurityModel.delete_security(portfolio_name, security_ticker)
            except Exception as e:
                return {"message": "An error occurred while delete the item."}, 500
        else:
            return {'message': "An item with ticker '{}' does not exists.".format(security_ticker.upper())}, 400
        return {"message": "'{}' has been deleted successfully.".format(data['ticker'].upper())}, 201
