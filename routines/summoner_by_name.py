from BSW_TFT.extractor.summoner import Summoner 



def get_summoners_by_name(summoner_name_list):
    
    summoner_object_list = []
    
    for summoner_r_obj in summoner_name_list:
        summoner = Summoner(summoner_r_obj['region'])
        summoner_obj = summoner.get_summoner_by_name(summoner_r_obj['name'])
        
        if summoner_obj == 'exception':
            break
            
        summoner_object_list.append(summoner_obj)

    return summoner_object_list 



