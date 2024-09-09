from dataclasses import dataclass, field

@dataclass
class JsonConfig:
    appDbConnStr: str = field(default="")
    db_host: str = field(default="localhost")
    db_name: int = field(default="db")
    db_username: str = field(default="uname")
    db_password: str = field(default="pwd")
    flaskSecret: str = field(default="")
    mode: str = field(default="")
    flask_port: int = field(default="1")
    latestatestRecommendationFetchUrl: str = field(default="")