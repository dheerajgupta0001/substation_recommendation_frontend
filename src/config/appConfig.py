import pandas as pd
import json
from src.config.jsonConfig import JsonConfig

def loadJsonConfig(fName="config.json") -> JsonConfig:
    global jsonConfig
    with open(fName) as f:
        data = json.load(f)
        jsonConfig = JsonConfig(**data)
        return jsonConfig


def getJsonConfig() -> JsonConfig:
    global jsonConfig
    return jsonConfig