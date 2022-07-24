import BSW_TFT.config as config
import requests
from BSW_TFT.extractor.utils import verify_request


class League:

    def __init__(self, region, save_mode="file"):

        self.save_mode = save_mode
        self.region = region
        self.base_url = config.BASE_URL.format(region=self.region, api_name='league', api_call='{api_call}')
        self.data_list = []

    def get_high_elo(self):

        for league in config.LEAGUES['high_elo']:

            r = requests.get(
                self.base_url.format(api_call=league),
                headers=config.HEADER
            )

            verify_request(request=r)

            league_data = r.json()
            league_data['region'] = self.region
            print(league_data)
            self.data_list.append(league_data)

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

                self.data_list.append(obj)


