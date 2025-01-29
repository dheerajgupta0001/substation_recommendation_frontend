from typing import TypedDict


class IPqVqViolationFetchResp(TypedDict):
    isSuccess: bool
    status: int
    message: str
    data: list