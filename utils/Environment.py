
from utils.JsonReader import JsonReader

class Environment:
    __instance = False
    __data=None

    @staticmethod
    def get_environment(environment):
        if not Environment.__instance:
            file = './resources/configs/' + environment + '.json'
            Environment.__data = JsonReader().getData(file)
            Environment.__instance=True
        return Environment.__data.copy()