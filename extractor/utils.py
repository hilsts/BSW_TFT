# TODO: MongoDB Class
#TODO: MariaDB Class
from pymongo import MongoClient
import configparser
import config
import requests
import time


class MongoDB:

    def __init__(self, collection):

        config = configparser.ConfigParser()
        config.read('/home/hilsts/config.ini')
        client = MongoClient('localhost', 27017)
        self.collection_obj = client[config['MONGODB']['dbname']][collection]

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

class API:

    def __init__(self):

        self.header = config.HEADER

    def get_from_url(self, url):

        r = requests.get(url, headers=self.header)

        if r.status_code == 200:

            print(url)
            print(r.json())
            return r.json()

        else:

            print(f'dormindo no get: {url}')
            time.sleep(200)
            return self.get_from_url(url)



MongoDB('league_summoner')



        


