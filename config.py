import configparser


CONFIG_PATH = '/home/hilsts/config.ini'

config = configparser.ConfigParser()
config.read(CONFIG_PATH)

API_KEY = config['API']['key']

# Configs

REGIONS = ['br1', 'eun1', 'euw1', 'jp1', 'kr', 'la1', 'la2', 'na1', 'oc1', 'ru', 'tr1']
LEAGUES = {
    'highelo' : ['challenger', 'grandmaster', 'master'],
    'lowelo' : ['diamond', 'platinum', 'gold', 'silver', 'bronze', 'iron'],
    'tiers' : ['I', 'II', 'III', 'IV']
           }


#API

BASE_URL = 'https://{region}.api.riotgames.com/tft/{api_name}/v1/{api_call}'

#TFT-LEAGUE-V1


HEADER = {
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:85.0) Gecko/20100101 Firefox/85.0",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Charset": "application/x-www-form-urlencoded; charset=UTF-8",
    "Origin": "https://developer.riotgames.com",
    "X-Riot-Token": "{API_KEY}".format(API_KEY=API_KEY)
    }

LEAGUE_CHALLENGER_URL = BASE_URL.format(api_name='league', api_call='challenger', region='{region}')
LEAGUE_GRANDMASTER_URL = BASE_URL.format(api_name='league', api_call='grandmaster', region='{region}')
LEAGUE_MASTER_URL = BASE_URL.format(api_name='league', api_call='master', region='{region}')
LEAGUE_TIERS_URL = BASE_URL.format(api_name='league', api_call='entries/{tier}/{division}', region='{region}')

print(LEAGUE_MASTER_URL)
print(LEAGUE_GRANDMASTER_URL)
print(LEAGUE_CHALLENGER_URL)
print(LEAGUE_TIERS_URL)
print(API_KEY)