import requests
import pandas as pd
import configparser
import json
import time
from datetime import datetime

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
    # TODO: Abstract league and region
    # TODO: Verification system
    def __init__(self):

        self.get_challengers_data()
        self.get_summoners_data()
        self.get_matches_by_summoner()

    def get_challengers_data(self):
        """
        Pega informações dos players do challenger no dia
        :return: challengers_df
        """

        challengers_data = requests.get('https://br1.api.riotgames.com/tft/league/v1/challenger', headers=HEADER)
        self.challengers_df = pd.DataFrame(challengers_data.json()['entries'])

    def get_summoners_data(self):
        """
        Para cada jogador no df de jogadores pega os dados de summoner
        :return: summ_data_df
        """

        summ_list = []
        for summ in self.challengers_df['summonerId'].tolist():

            summ_data = requests.get(f'https://br1.api.riotgames.com/tft/summoner/v1/summoners/{summ}', headers=HEADER)
            summ_list.append(summ_data.json())

        summ_data_df = pd.DataFrame(summ_list)

        self.summ_joined = pd.merge(self.challengers_df, summ_data_df, left_on='summonerId', right_on='id', how='inner')
        self.summ_joined.to_csv(f'data/challengers_data/joined_temp_{datetime.today()}.csv')
        print(self.summ_joined)

    def get_matches_by_summoner(self):
        """
        Para cada jogador pega os ids das partidas
        :return:
        """

        df = pd.read_csv('data/challengers_data/joined_temp.csv')
        matches_list = []
        for puuid in df['puuid'].tolist():
            matches_by_summ = requests.get(
                f'https://americas.api.riotgames.com/tft/match/v1/matches/by-puuid/{puuid}/ids?count=500',
                headers=HEADER)
            print(len(matches_by_summ.json()))

            matches_list = list(set(matches_list + matches_by_summ.json()))


        matches_id_df = pd.DataFrame(matches_list)

        matches_id_df.to_csv('data/challengers_data/matches_ids.csv')


class PlayerData():

    def __init__(self, name):

        self.name = name
        self.get_player_ids()
        self.get_player_matches()
    def get_player_ids(self):


        print(f'getting player_ids for {self.name}')
        player_ids = requests.get(f'https://br1.api.riotgames.com/tft/summoner/v1/summoners/by-name/{self.name}',
                                  headers=HEADER)

        print(player_ids.json())
        self.player_ids = player_ids.json()

    def get_player_matches(self):

        puuid = self.player_ids['puuid']
        print(puuid)

        player_matches = requests.get(
            f'https://americas.api.riotgames.com/tft/match/v1/matches/by-puuid/OAYf88iAsSwE1bWxVf9wTSKE-ugoEMNVG_PBDuU3FM3ObSiqfzTHFnutIaaDKR4Pdr8iE4AtSfqpjw/ids?count=200',
            headers=HEADER
        )

        print(player_matches.status_code)
        print(player_matches.json())
        print(len(player_matches.json()))
        pd.DataFrame(player_matches.json()).to_csv(
            f'data/matches/{self.name}_match_ids.csv')





class MatchData:

    def __init__(self, matches):

        self.match_list = matches
        self.verified_matches = self.verify_old_matches()
        self.get_match_data()

    def verify_old_matches(self):
        """
        Compare matches on db with matches wanted to get
        :return: verified_matches (list)
        """

        try:
            old_matches = pd.read_csv('data/matches/full_matches.csv').tolist()
            return list(set(self.match_list + old_matches))

        except:
            print('verify exception')
            return self.match_list

    def get_match_data(self):
        """

        :return:
        """

        data_list = []
        for match in self.verified_matches:
            match_data = requests.get(f'https://americas.api.riotgames.com/tft/match/v1/matches/{match}',
                                      headers=HEADER)

            if match_data.status_code == 200:
                data_list.append(match_data.json())

                print(match_data.json())

            else:
                print('dormindo...')
                time.sleep(120)
                print('acordando...')

        with open('data/raw_matchdata.json', 'w') as outfile:
            json.dump(data_list, outfile)




matches = pd.read_csv('data/matches/Tataba_match_ids.csv', index_col=[0])['0'].tolist()\
#
MatchData(matches=matches)


# PlayerData('Tataba')