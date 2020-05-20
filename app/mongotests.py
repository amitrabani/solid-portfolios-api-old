import pymongo
import json

class DB(object):

    URI = "mongodb+srv://amitke02:12nhnh@cluster0-zllqr.mongodb.net/test?retryWrites=true&w=majority"

    @staticmethod
    def init():
        client = pymongo.MongoClient(DB.URI)
        DB.DATABASE = client['solid_porfolio']

    @staticmethod
    def insert(collection, data):
        DB.DATABASE[collection].insert_security(data)

    @staticmethod
    def find_one(collection, query):
        return DB.DATABASE[collection].find_one(query)


    @staticmethod
    def find_all():
        return list(DB.DATABASE["securities"].find())


    @staticmethod
    def insert_to_array_in_document(collection, query, new_values):
        DB.DATABASE[collection].update_one(query, new_values)

    @staticmethod
    def find_one_in_array(collection, document_query, array_query):
        return DB.DATABASE[collection].find_one(document_query,array_query)

    @staticmethod
    def update_one_in_array(collection, document_query, array_update_query):
        try:
            DB.DATABASE[collection].update_one(document_query, array_update_query)
        except Exception as e:
            print(e)

    @staticmethod
    def delete_one_in_array():
        document_query = {"portfolio_name": "AMIT"}
        array_update_query =  {"$pull": {"securities": {"ticker": "TEVA "}}}
        DB.DATABASE["portfolios"].update_one(document_query, array_update_query)

DB.init()
DB.delete_one_in_array()
# DB.insert_to_array_in_document("portfolios", "AMIT", "securities", security)
# document_query = {"portfolio_name": "AMIT", "securities.ticker": "TEVA"}


# array_update_query = {"$inc": {"securities.$.amount": 4}}
# DB.update_one_in_array("portfolios", document_query, array_update_query)

# query = {"portfolio_name": portfolio_name}
# new_values = {'$push': {'securities': security}}

#
# document_query = {"portfolio_name": "AMIT"}
# array_query = {"securities": {"$elemMatch": {"ticker": "TSLA"}}}
