from utils import MongoDB
import config

class League:

    def __init__(self, region):

        self.region = region
        self.base_url = config.BASE_URL.format(region=self.region, api_name='league', api_call='{api_call}')


    def get_highelos(self):

        print(config.LEAGUES)
        for league in config.LEAGUES['highelo']:

            print(self.base_url.format(api_call=league))



League('br1').get_highelos()



