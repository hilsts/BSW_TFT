from extractor.region import Region
from extractor.league import League

# TODO: First full pipeline, region to league range. Create filesystem and save all leagues.

def extract_league():
    region = Region()

    for reg in region.regions_list:
        league = League(reg)
        league.get_high_elo()

extract_league()