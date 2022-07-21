#from pymongo import MongoClient
import BSW_TFT.config as config
import json
from datetime import datetime
import os
import time



# class MongoDB:

#     def __init__(self, collection):

#         mongo = config.MONGO_CONFIG
#         client = MongoClient(mongo['host'], mongo['port'])
#         self.collection_obj = client[mongo['dbname']][collection]

#     def verify_first(self):

#         if self.collection_obj.count_documents({}) == 0:
#             return True
#         else:
#             return False

#     def insert_one(self, document):

#         return self.collection_obj.insert_one(document)

#     def insert_documents(self, document_list):

#         return self.collection_obj.insert_many(document_list)

#     def query_documents(self, query):

#         return self.collection_obj.find(query)


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


def verify_request(request):

    if request.status_code == 200:

        pass

    if request.status_code == 503:
        time.sleep(300)
    


