## Mongo DAO(Data access object)

from pymongo import MongoClient
import os
from bson.objectid import ObjectId

"""
Use DAO to interface backend code with MongoDB
get_one - retrieve one document from collection
get_all - retrieve all documents from collection matching the condition
update  - update document in collection
insert  - insert document into collection 
"""


class database:

    def __init__(self):

        self.host = 'localhost'
        self.port = '27017'
        self.database = 'BabbleZ'

        self.client = MongoClient(f'mongodb://{self.host}:{self.port}')

    # host = os.environ.get('MONGO_HOST') or 'localhost'
    # port = os.environ.get('MONGO_PORT') or '27017'
    # username = os.environ.get('MONGO_USERNAME') or 'admin'
    # password = os.environ.get('MONGO_PASSWORD') or 'admin'
    # database = os.environ.get('MONGO_DB') or 'BabbleZ'

    # client = MongoClient('mongodb://' + username + ':' + password + '@' + host + ':' + str(port) + '/admin')
    # client = MongoClient(f'mongodb://{host}:{port}')

    # CRUD for Mongo

    # Insert
    def insert(self, collection, json):
        return str(self.client[self.database][collection].insert(json))

    # Update
    def update(self, collection, _id, dic):
        self.client[self.database][collection].update_one({'_id': ObjectId(_id)}, {"$set": dic}, upsert=True)

    # Get all
    def get_all(self, collection, filter_field, filter_value):
        final_results = []
        results = self.client[self.database][collection].find({filter_field: filter_value})
        for result in results:
            final_results.append(str(result))
        return final_results

    # Get One
    def get_one(self, collection, filter_field, filter_value):
        results = self.client[self.database][collection].find({filter_field: filter_value})
        for result in results:
            return result

    # Get collection
    def get_collection(self, collection):
        results = self.client[self.database][collection].find({})
        for result in results:
            return result

    # search
    def search_one(self, collection, json):
        results = self.client[self.database][collection].find(json)
        for result in results:
            return result

    # Get by id
    def get_by_id(self, collection, _id):
        results = self.client[self.database][collection].find({"_id": ObjectId(_id)})
        for result in results:
            return result

    # Delete
    def delete(self, collection, _id):
        self.client[self.database][collection].delete_one({"_id": ObjectId(_id)})


if __name__ == '__main__':
    pass
