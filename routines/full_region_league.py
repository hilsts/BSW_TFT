from BSW_TFT.extractor.region import Region
from BSW_TFT.extractor.league import League

# TODO: First full pipeline, region to league range. Create filesystem and save all leagues.

def extract_league():
    region = Region()
    region.create_folders()
    
    league_list = []
    for reg in region.regions_list:
        league = League(reg)
        league.get_high_elo()
        
        league_list.append(league.data_list)

    return league_list
        