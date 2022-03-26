import config
import requests
from utils import MongoDB

class Summoner:

    def __init__(self, region):

        self.region = region
        self.base_url = config.SUMMONER_BY_ID.format(region=region)
        self.mongo_league = MongoDB('league')
        self.mongo_summoner = MongoDB('summoner')

    def get_summoners_from_db(self):

        league_docs = self.mongo_league.query_documents({'tier' : 'SILVER', 'division' : {'$in' : ['I', 'II', 'III', 'IV']}})

        # for league in league_docs:
        #     for summoner in league['entries']:
        #         try:
        #             x = summoner['summonerId']
        #
        #         except Exception as e:
        #             print(e)
        #             print(summoner)
        #             print(league['_id'])
        #
        #             print('\n')

        for k in league_docs:
            for i in k['entries']:
            # print(type(i))
                if type(i) == dict:
                    print(i['summonerId'])
                else:
                    print(i)
                    print(type(i))

    def get_summoner_by_id(self, summoner_id):

        # TODO: verify and get of summoners



