from BSW_TFT.extractor.match import Match
from BSW_TFT.extractor.summoner import Summoner
import BSW_TFT.config as config



def matches_by_name(summoner_name, region='br1'):

    summoner_obj = Summoner(region=region)

    summoner_json = summoner_obj.get_summoner_by_name(summoner_name=summoner_name)

    print(summoner_json)
    matches_obj = Match(region=region)

    matches_json = matches_obj.get_matches(puuid=summoner_json['puuid'], count=200)

    match_list = []

    for match_id in matches_json:

        match_obj = matches_obj.get_match(match_id=match_id)

        match_list.append(match_obj)

    return match_list

 




    
