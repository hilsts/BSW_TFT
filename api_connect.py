import requests
import pandas as pd
import configparser

config = configparser.ConfigParser()
config.read('config.ini')

API_KEY = config['API']['key']

HEADER = {
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:85.0) Gecko/20100101 Firefox/85.0",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Charset": "application/x-www-form-urlencoded; charset=UTF-8",
    "Origin": "https://developer.riotgames.com",
    "X-Riot-Token": "{API_KEY}".format(API_KEY=API_KEY)
    }

class ChallengerPlayers:

    def __init__(self):

        self.summoners_ids = self.get_challengers_data()
        self.puuids = self.get_puuids()

    def get_challengers_data(self):
        """

        :return:
        """

        from datetime import date
        challengers_data = requests.get('https://br1.api.riotgames.com/tft/league/v1/challenger', headers=HEADER)
        df = pd.DataFrame(challengers_data.json()['entries'])
        df.to_csv(f'data/challengers_data/{str(date.today())}.csv')

        return df['summonerId'].unique().tolist()

    def get_puuids(self):
        """

        :return:
        """




ChallengerPlayers()

