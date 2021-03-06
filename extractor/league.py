import config
import requests
from utils import MongoDB

class League:

    def __init__(self, region):

        self.region = region
        self.base_url = config.BASE_URL.format(region=self.region, api_name='league', api_call='{api_call}')
        self.mongo_client = MongoDB('league')

    def get_high_elo(self):

        for league in config.LEAGUES['high_elo']:


            r = requests.get(
                self.base_url.format(api_call=league),
                headers=config.HEADER
            )

            league_data = r.json()
            x = self.mongo_client.insert_one(league_data)
            print(x.inserted_id)

    def get_low_elo(self):

        for league in config.LEAGUES['low_elo']:
            for tier in config.LEAGUES['tiers']:

                temp_ = []
                page = 1

                print(league)
                print(tier)
                league_tier_url = config.LEAGUE_TIERS_URL.format(region=self.region,
                                                     tier=league,
                                                     division=tier)

                league_tier_url_p =  league_tier_url + f'?page={page}'

                r = requests.get(
                    league_tier_url_p,
                    headers=config.HEADER
                )

                temp_ += r.json()

                while len(r.json()) != 0:

                    page += 1
                    league_tier_url_p = league_tier_url + f'?page={page}'
                    print(league_tier_url_p)
                    r = requests.get(
                        league_tier_url_p,
                        headers=config.HEADER
                    )
                    temp_ += r.json()

                x = self.mongo_client.insert_one(
                    {
                        'region' : self.region,
                        'tier': league,
                        'division': tier,
                        'entries': temp_
                    }
                )

                print(x.inserted_id)




League('br1').get_low_elo()
League('br1').get_high_elo()




