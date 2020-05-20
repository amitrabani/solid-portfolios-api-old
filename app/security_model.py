import datetime
from database import DB

class SecurityModel(object):
    @classmethod
    def find_object_in_db(cls, collection, security_ticker):
        return DB.find_one(collection, security_ticker)

    @staticmethod
    def change_securities_amount(portfolio_name, security_ticker, security_amount):
        document_query = {"portfolio_name": portfolio_name, "securities.ticker": security_ticker}
        array_update_query = {"$inc": {"securities.$.amount": security_amount}}
        return DB.update_one_in_array("portfolios", document_query, array_update_query)

    @staticmethod
    def get_all_objects_in_db():
        return DB.find_all("portfolios")

    @staticmethod
    def find_one_in_array(portfolio_name, security_ticker):
        document_query = {"portfolio_name": portfolio_name}
        array_query = {"securities": {"$elemMatch": {"ticker": security_ticker}}}
        return DB.find_one_in_array("portfolios", document_query, array_query)


    @staticmethod
    def delete_security(portfolio_name, security_ticker):
        document_query = {"portfolio_name": portfolio_name}
        array_update_query =  {"$pull": {"securities": {"ticker": security_ticker}}}
        DB.delete_one_in_array("portfolios", document_query, array_update_query)

    @staticmethod
    def insert_security(security_details, portfolio_name):
        security = {
            'ticker': security_details['symbol'],
            'price': security_details['price']['regularMarketOpen']['raw'],
            'name': security_details['price']['shortName'],
            'amount': 0,
            'added_date': datetime.datetime.now().isoformat()
        }
        query = {"portfolio_name": portfolio_name}
        new_values = {'$push': {'securities': security}}
        DB.insert_to_array_in_document("portfolios", query, new_values)
