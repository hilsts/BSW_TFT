import BSW_TFT.config as config
from BSW_TFT.extractor.utils import FileSystem


class Region:

    def __init__(self):
        self.regions_list = config.REGIONS

    def create_folders(self):

        fs = FileSystem()

        if fs.verify_root():
            return 0
        else:
            fs.create_dir('')
            for region in self.regions_list:
                fs.create_dir(region)
