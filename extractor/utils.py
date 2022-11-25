from cmath import pi
from pymongo import MongoClient
import config as config
import json
from datetime import datetime
import os


class MongoDB:

    def __init__(self, collection):

        mongo = config.MONGO_CONFIG
        print(type(mongo['port']))
        client = MongoClient(f'mongodb+srv://{mongo["user"]}:{mongo["pwd"]}@bswtft1.woebl.mongodb.net/?retryWrites=true&w=majority')
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

    def query_documents(self, query, projection):

        return self.collection_obj.find(filter=query, projection=projection)

    def delete_documents(self, query):

        return self.collection_obj.delete_many(query)

    def aggregate(self, pipeline):

        return self.collection_obj.aggregate(pipeline=pipeline)

class FileSystem():

    def __init__(self):

        self.root_path = config.FILE_SYSTEM_ROOT

    def write_to_path(self, path, document):
        try:
            print('write to path')
            print(self.root_path+path)
            with open(self.root_path+path, 'w') as json_file:
                json.dump(document, json_file)
        except FileNotFoundError:
            print('except')


            dir_path = self.contruct_path(self.name, root=True)
            os.mkdir(self.root_path+dir_path)
            file_path = self.contruct_path(self.name)
            self.write_to_path(file_path, document)

    def contruct_path(self, name, root=False):
        self.name = name
        # TODO: construct save_path to filesystem
        if root:
            print(f'root: {name}')
            return f'/{name}/'

        print(f'/{name}/{datetime.now()}.json')
        return f'{name}/{datetime.now()}.json'

    def create_dir(self, path):

        os.mkdir(self.root_path + path)

    def verify_root(self):

        return os.path.isdir(config.FILE_SYSTEM_ROOT)


def verify_response(response):

    status_code = response.status_code

    if status_code == 200:

        return response.json()


    else:
        data = response.json()
        data['retry_url'] = response.url
        return data