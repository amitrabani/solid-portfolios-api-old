import pymongo

class DB(object):

    URI = "mongodb+srv://amitke02:12nhnh@cluster0-zllqr.mongodb.net/test?retryWrites=true&w=majority"

    @staticmethod
    def init():
        client = pymongo.MongoClient(DB.URI)
        DB.DATABASE = client['solid_porfolio']

    @staticmethod
    def insert(collection, data):
        DB.DATABASE[collection].insert(data)

    @staticmethod
    def insert_to_array_in_document(collection, query, new_values):
        try:
            DB.DATABASE[collection].update_one(query, new_values)
        except Exception as e:
            print(e)

    @staticmethod
    def update_one_in_array(collection, document_query, array_update_query):
        DB.DATABASE[collection].update_one(document_query, array_update_query)

    @staticmethod
    def find_one(collection, query):
        return DB.DATABASE[collection].find_one(query)

    @staticmethod
    def find_one_in_array(collection, document_query, array_query):
        return DB.DATABASE[collection].find_one(document_query,array_query)

    @staticmethod
    def update_one(security_ticker, buying_amount):
        DB.DATABASE["securities"].update_one({"ticker": security_ticker}, {"$inc": {"amount": buying_amount}})

    @staticmethod
    def find_all(collection):
        return DB.DATABASE[collection].find()

    @staticmethod
    def delete_one(ticker):
        DB.DATABASE["securities"].delete_one({'ticker': ticker})

    @staticmethod
    def insert_portfolio(collection, portfolio_name):
        DB.DATABASE[collection].insert_security(portfolio_name)

    @staticmethod
    def delete_one_in_array(collection, document_query, array_update_query):
        DB.DATABASE[collection].update_one(document_query, array_update_query)
