from typing import TypedDict
import datetime as dt


class ILatestRecommendationSummary(TypedDict):
    id: str
    time_stamp: dt.datetime
    substation_name: str
    recommendation: str
    voltage_str: str