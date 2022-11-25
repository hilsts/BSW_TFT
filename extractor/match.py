import config as config
import requests
from extractor.utils import verify_request

class Match:

    def __init__(self, region):
        
        
        self.region_map = {
            'br1' : 'AMERICAS', 
            'eun1' : 'EUROPE', 
            'euw1' : 'EUROPE', 
            'jp1' : 'ASIA', 
            'kr' : 'ASIA', 
            'la1' : 'AMERICAS', 
            'la2' : 'AMERICAS', 
            'na1' : 'AMERICAS', 
            'oc1' : 'SEA', 
            'ru' : 'EUROPE', 
            'tr1' : 'EUROPE'
        }

        self.region = self.region_map[region]

    def get_matches(self, puuid, start=0, count=20, end_time=None, start_time=None):
        
        match_base = config.MATCHES_URL.format(
                puuid=puuid,
                region=self.region,
                count=count,
                start=start
            )
        
        print(f'match_base: {match_base}')

        if start_time != None:

            match_base = match_base + f'&end_time={end_time}&start_time={start_time}'


        r = requests.get(
            url=match_base,
            headers=config.HEADER
        )

        verify_request(r)

        return r.json()

    def get_match(self, match_id):

        match_base_url = config.MATCH_URL.format(
            match_id=match_id,
            region=self.region
        )

        r = requests.get(
            url=match_base_url,
            headers=config.HEADER
        )

        return r.json()