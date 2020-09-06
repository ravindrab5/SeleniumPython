import json
from utils.LogInitilizer import LogInitilizer
logger=LogInitilizer.getLogger()

class JsonReader:

    def getData(self,pathtofile):
        with open(pathtofile) as f:
            data=json.load(f)
            logger.debug("Data from file {}  -  {}".format(pathtofile, data))
            return data