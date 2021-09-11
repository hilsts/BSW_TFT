import config

from utils import MongoDB, API

class Summoner:

    def __init__(self, region):

        self.region = region
        self.base_url = config.SUMMONER_BY_ID.format(region=region)
        self.mongo_league = MongoDB('league')
        self.mongo_summoner = MongoDB('summoner')

    def get_summoners_from_db(self):

        league_docs = self.mongo_league.query_documents({})

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


        c = 0
        for k in league_docs:
            for i in k['entries']:

                if type(i) == dict:

                    print(i['summonerId'])
                    c+=1
                    summoner_url = config.SUMMONER_BY_ID.format(
                        region=self.region
                    ) + f"/{i['summonerId']}"

                    api = API()
                    summoner_data = api.get_from_url(summoner_url)
                    print(type(summoner_data))
                    self.mongo_summoner.insert_one(summoner_data)

                else:
                    print(i)
                    print(type(i))

        print(c)
    def get_summoner_by_id(self, summoner_id):

        print(self.mongo_summoner.collection_obj.count_documents({}))


# api = API()
#
# x = api.get_from_url('https://br1.api.riotgames.com/tft/summoner/v1/summoners/3lDseDIm37wABQZJtq2-Nlj0uw8j-XXWDnL7zjQpKXqyJq8')
# print(type(x))

Summoner('br1').get_summoner_by_id(1)