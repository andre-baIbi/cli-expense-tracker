import configparser
import json
from argparse import Namespace
from configparser import ConfigParser
from copy import deepcopy

from Category import Category


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

def deleteById(_id: str, fileHandler: FileHandler):
    data = fileHandler.parseDataFromJsonFile()
    del data[_id]
    fileHandler.saveDataInJsonFile(data)


def updateExpenseInDataFile(argsFromCli: Namespace, fileHandler: FileHandler):
    argsId = str(argsFromCli.id)

    data = fileHandler.parseDataFromJsonFile()
    expenseData = data[argsId]
    for argName in argsFromCli.__dir__():
        if argName and (not "_" in argName):
            arg = argsFromCli.__getattribute__(argName)
            if arg and (not arg == "id"):
                expenseData[argName] = str(arg)
    data[argsId] = expenseData
    fileHandler.saveDataInJsonFile(data)


def firstRunListPrint(data):
    print()
    for key, _ in deepcopy(data).popitem()[1].items():
        print(key.upper(), end="    ")
    print()


def listAllExpenses(fileHandler: FileHandler, printable=None) -> list[dict]:
    expenses = []
    data = fileHandler.parseDataFromJsonFile()

    if printable: firstRunListPrint(data)
    for expenseDict in data.values():
        for k, v in expenseDict.items():
            if printable: print(v, end="    ")
        expenses.append(expenseDict)
        if printable: print()
    return expenses

def summaryOfExpenses(fileHandler: FileHandler, _filterByCategory: Category=None):
    _sum = 0
    for expense in listAllExpenses(fileHandler):
        if _filterByCategory and expense["category"] == _filterByCategory.value: continue
        for key, value in expense.items():
            if key == "amount":
                _sum += float(value)
    return _sum

if __name__ == '__main__':
    ...