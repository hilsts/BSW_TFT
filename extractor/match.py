import BSW_TFT.config as config
import requests
from BSW_TFT.extractor.utils import verify_request

class Match:

    def __init__(self, region):


        self.region = region

    def get_matches(self, puuid, start=0, count=20, end_time=None, start_time=None):
        
        match_base = config.MATCHES_URL.format(
                puuid=puuid,
                region=self.region,
                count=count,
                start=start
            )

        if start_time != None:

            match_base = match_base + f'&end_time={end_time}&start_time={start_time}'


        r = requests.get(
            url=match_base,
            headers=config.HEADER
        )

        verify_request(r)

        return r.json()