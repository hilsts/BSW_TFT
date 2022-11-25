import config as config
import requests
from extractor.utils import MongoDB, verify_response


class League:

    def __init__(self, region, save_mode="file"):

        self.save_mode = save_mode
        self.region = region
        self.base_url = config.BASE_URL.format(region=self.region, api_name='league', api_call='{api_call}')

    def get_high_elo(self):

        for league in config.LEAGUES['high_elo']:

            r = requests.get(
                self.base_url.format(api_call=league),
                headers=config.HEADER
            )

            league_data = verify_response(r)

            league_data['region'] = self.region
            print(league_data)
            self.save(league_data)

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

                league_tier_url_p = league_tier_url + f'?page={page}'

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

                obj = {
                        'region': self.region,
                        'tier': league,
                        'division': tier,
                        'entries': temp_
                    }

                self.save(obj)

    def save(self, obj):

        self.mongo_client = MongoDB('league')
        x = self.mongo_client.insert_one(obj)
        print(x.inserted_id)

