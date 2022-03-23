import config
from utils import FileSystem


class Region:

    def __init__(self):
        self.regions_list = config.REGIONS

    def create_folders(self):



        fs = FileSystem()

        fs.create_dir('')
        for region in self.regions_list:
            fs.create_dir(region)


Region().create_folders()