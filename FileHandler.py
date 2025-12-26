import configparser
import json
from configparser import ConfigParser


class FileHandler:
    config: ConfigParser
    CONFIG_FILENAME = "config.ini"
    jsonFilename = "data.json"

    def __init__(self, env):
        self.config = configparser.ConfigParser()
        self.config.read(self.CONFIG_FILENAME)
        self.env = env
        if env == "test":
            self.jsonFilename = "test_data.json"

    @classmethod
    def getFileHandler(cls, env):
        return cls(env)

    def getLatestId(self):
        latestIdKey = "latest_id"

        if self.env == "test":
            latestIdKey = "test_latest_id"


        latestId = int(self.config["SETTINGS"][latestIdKey])

        self.config["SETTINGS"][latestIdKey] = str(int(self.config["SETTINGS"][latestIdKey]) + 1)
        with open(self.CONFIG_FILENAME, "w") as config_file:
            self.config.write(config_file)

        return latestId

    def getDataFilenameFromConfig(self):
        return self.config["SETTINGS"]["json_filename"]


    def parseDataFromJsonFile(self):
        try:
            with open(self.jsonFilename, "r") as jsonFile:
                return json.load(jsonFile)
        except FileNotFoundError:
            with open(self.jsonFilename, "w") as _:
                return {}

    def saveDataInJsonFile(self, data: dict):
        with open(self.jsonFilename, "w") as jsonFile:
            json.dump(data, jsonFile)

    def getById(self, _id: int):
        return self.parseDataFromJsonFile()[str(_id)]


if __name__ == '__main__':
    ...