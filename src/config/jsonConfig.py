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
    latestatestRecommendationFetchUrl: str = field(default=""),
    pqVqViolationFetchUrl: str = field(default=""),
    oauth_app_client_id: str = field(default="")
    oauth_app_client_secret: str = field(default="")
    oauth_provider_discovery_url: str = field(default="")