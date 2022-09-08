from BSW_TFT.extractor.region import Region
from BSW_TFT.extractor.league import League


def extract_league():
    region = Region()
    
    league_list = []
    for reg in region.regions_list:
        league = League(reg)
        league.get_high_elo()
        league.get_low_elo()
        
        league_list.append(league.data_list)

    return league_list
        