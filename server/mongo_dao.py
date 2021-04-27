# Mongo DAO(Data access object)

from pymongo import MongoClient
from bson.objectid import ObjectId

"""
Use DAO to interface backend code with MongoDB
get_one - retrieve one document from collection
get_all - retrieve all documents from collection matching the condition
update  - update document in collection
insert  - insert document into collection 
"""


class MongoDAO:

    def __init__(self, db='BabbleZ'):

        self.host = 'localhost'
        self.port = '9000'#                '27017'
        self.database = db

        self.db_client = MongoClient(f'mongodb://{self.host}:{self.port}')

    # CRUD for Mongo

    # Insert
    def insert(self, collection, json):

        obj_id = self.db_client[self.database][collection].insert(json)
        return str(obj_id)

    # Update
    def update(self, collection, _id, dic):
        self.db_client[self.database][collection].update_one({'_id': ObjectId(_id)}, {"$set": dic}, upsert=True)

    # Update by field
    def update_by(self, collection, attribute, value, dic):
        self.db_client[self.database][collection].update_one({attribute: value}, {"$set": dic}, upsert=True)

    # Get all
    def get_all(self, collection, filter_field, filter_value):
        final_results = []
        results = self.db_client[self.database][collection].find({filter_field: filter_value})
        for result in results:
            final_results.append(str(result))
        return final_results

    # Get One
    def get_one(self, collection, filter_field, filter_value):
        results = self.db_client[self.database][collection].find({filter_field: filter_value})
        for result in results:
            return result

    # Get collection
    def get_collection(self, collection):
        results = self.db_client[self.database][collection].find({})
        final_results = []
        for result in results:
            final_results.append(result)
        return final_results

    # search
    def search_one(self, collection, json):
        results = self.db_client[self.database][collection].find(json)
        for result in results:
            return result

    # Get by id
    def get_by_id(self, collection, _id):
        results = self.db_client[self.database][collection].find({"_id": ObjectId(_id)})
        for result in results:
            return result

    # Delete
    def delete(self, collection, _id):
        self.db_client[self.database][collection].delete_one({"_id": ObjectId(_id)})

    # Derived

    # Get Public Key Local DB
    def get_publicKey(self, user_id):
        return self.get_one('Profiles', 'user_id', user_id)["public_key"]

    # Check for User In Local DB
    def if_user_exist(self, user_id):
        if self.search_one('Profiles', {"user_id": user_id}):
            return True
        else:
            return False

    # Check If Friend Data Exist
    def if_friend_exist(self, user_id):
        if self.search_one('Friend', {"user_id": user_id}):
            return True
        else:
            return False

    # Get My Hashed Password
    def get_user_password(self, user_id):
        return self.get_one("Profiles", "user_id", user_id)["password"]

    # Messaging
    # Saving to Database
    def imprint_message(self, msg_type: str, metadata: list, payload: str):

        collection = metadata[0]

        date_time = str(ObjectId(metadata[2]).generation_time)[:-6]

        js_obj = {"type": msg_type,
                  "date": str(date_time),
                  "size": metadata[1],
                  "payload": payload
                  }

        return self.insert(collection, js_obj)

    # Reading from Database
    def read_scriptures(self, userid):

        msg_list = self.get_collection(userid)
        msg_list.sort(key=lambda arg: arg["_id"], reverse=True)
        return msg_list


if __name__ == '__main__':

    # Testing Program

    obj = MongoDAO()

    lis = obj.read_scriptures("mnChar_akash")
    for i in lis:
        print(i)

'''
---------------------------
Stored Database Structure:
---------------------------
Database : BabbleZ
    Collection : Profile
    Collection : Friends

    Collection : user_id
        {
            "type": received/sent
            "date": ''
            "size" ''
            "payload" : ''
            "status" : ''
        }
---------------------------------------        
Incoming / Sending Packet Structure:   
---------------------------------------     
    payload:
    metadata:
        user_id
        size
        msg_id


'''