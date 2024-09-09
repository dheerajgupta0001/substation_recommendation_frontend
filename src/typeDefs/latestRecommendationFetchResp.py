from typing import TypedDict


class ILastestRecommendationFetchResp(TypedDict):
    isSuccess: bool
    status: int
    message: str
    data: list