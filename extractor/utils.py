from pymongo import MongoClient
import config
import json

class MongoDB:

    def __init__(self, collection):

        config = configparser.ConfigParser()
        mongo = config.MONGO_CONFIG
        client = MongoClient(mongo['host'], mongo['port'])
        self.collection_obj = client[mongo['dbname']][collection]

    def verify_first(self):

        if self.collection_obj.count_documents({}) == 0:
            return True
        else:
            return False

    def insert_one(self, document):

        return self.collection_obj.insert_one(document)

    def insert_documents(self, document_list):

        return self.collection_obj.insert_many(document_list)

    def query_documents(self, query):

        return self.collection_obj.find(query)


class FileSystem():

    def __init__(self):

        self.root_path = config.FILE_SYSTEM_ROOT

    def write_to_path(self, path, document):

        with open(self.root_path+path, 'w') as json_file:
            json.dump(document, json_file)


    def contruct_path(self):
        


