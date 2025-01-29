import pandas as pd
import json
from src.config.jsonConfig import JsonConfig

# initialize the app config global variable
jsonConfig = {}

def loadAppConfig(fName="config.json") -> JsonConfig:
    global jsonConfig
    with open(fName) as f:
        data = json.load(f)
        jsonConfig = JsonConfig(**data)
        return jsonConfig


def getAppConfig() -> JsonConfig:
    global jsonConfig
    return jsonConfig