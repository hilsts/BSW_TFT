from BSW_TFT.extractor.summoner import Summoner 



def get_summoners_by_name(summoner_name_list, region):
    
    summoner_object_list = []
    
    for summoner_name in summoner_name_list:
        summoner = Summoner(region)
        summoner_obj = summoner.get_summoner_by_name(summoner_name)
        summoner_object_list.append(summoner_obj)

    return summoner_object_list 



