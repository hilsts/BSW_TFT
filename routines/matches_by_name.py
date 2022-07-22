from BSW_TFT.extractor.match import Match
from BSW_TFT.extractor.match import Summoner
import BSW_TFT.config as config



def matches_by_name(summoner_name, region=config.REGION):

    summoner_obj = Summoner(region=region)

    summoner_json = summoner_obj.get_summoner_by_name(summoner_name=summoner_name)

    matches_obj = Match(region=region)

    matches_json = matches_obj.get_matches(puuid=summoner_json['puuid'], count=200)

    
