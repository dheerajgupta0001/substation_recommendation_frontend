from typing import TypedDict
import datetime as dt


class IPqVqViolationSummary(TypedDict):
    id: str
    time_stamp: dt.datetime
    generating_station: str
    voltage: float
    substation_mvar: float
    farm_p: float
    farm_q: float
    isVqViolated: bool
    isPqViolated: bool
    isPqVqViolated: bool