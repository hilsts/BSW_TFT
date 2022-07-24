import BSW_TFT.config as config
import requests

from BSW_TFT.extractor.utils import verify_request

class Summoner:

    def __init__(self, region):

        self.region = region


    def get_summoner_by_name(self, summoner_name):

        print(summoner_name)
        summoner_base_url = config.SUMMONER_BY_NAME.format(
            summoner_name=summoner_name,
            region = self.region
        )
        
        print(f'summoner_url: {summoner_base_url}')

        r = requests.get(
            url=summoner_base_url,
            headers=config.HEADER
        )

        verify_request(r)

        return r.json()
    
    ##def verify_eongo):xistence(self, summoner_name, m
        
        



