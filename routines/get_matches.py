import re
from BSW_TFT.extractor.match import Match

def get_matches_ids(puuid, region='br1'):

    matches_obj = Match(region=region)
    matches_json = matches_obj.get_matches(puuid=puuid, count=200)
    
    print(f'{puuid}, {len(matches_json)}')
    
    return matches_json

def get_matches(matches_ids, region='br1'):
    
    match_obj = Match(region=region)
    match_list = []
    
    for match_id in matches_ids:

        match_obj = match_obj.get_match(match_id=match_id)

        match_list.append(match_obj)
        
    return match_list
