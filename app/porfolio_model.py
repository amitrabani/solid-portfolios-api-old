from database import DB
from database import DB


class PortfolioModel(object):
    @classmethod
    def find_portfolio_in_db(cls, collection, portfolio_name):
        return DB.find_one(collection, portfolio_name)

    @staticmethod
    def get_all_objects_in_db():
        return DB.find_all("portfolios")

    #change to work on id
    @staticmethod
    def delete_portfolio(portfolio_name):
        DB.DATABASE["portfolios"].delete_one({'portfolio_name': portfolio_name})

    @staticmethod
    def insert_porfolio(portfolio_name):
        portfolio = {"portfolio_name": portfolio_name, "securities": []}
        DB.insert("portfolios", portfolio)
