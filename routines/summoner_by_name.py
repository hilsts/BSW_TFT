from BSW_TFT.extractor import Summoner 



def get_summoners_by_name(summoner_name_list, region):
    
    summoner = Summoner(region)
    summoner_obj = summoner.get_summoner_by_name(summoner_name)
    
    return summoner_obj

