import requests
import datetime as dt
from src.typeDefs.latestRecommendationFetchResp import ILastestRecommendationFetchResp

class LatestRecommendationFetcher():
    latestatestRecommendationFetchUrl = ''

    def __init__(self, latestatestRecommendationFetchUrl):
        self.latestatestRecommendationFetchUrl = latestatestRecommendationFetchUrl

    def fetchLatestRecommendation(self) -> ILastestRecommendationFetchResp:
        """_summary_

        Returns:
            ILastestRecommendationFetchResp: _description_
        """
        res = requests.get(self.latestatestRecommendationFetchUrl)

        operationResult: ILastestRecommendationFetchResp = {
            "isSuccess": False,
            'status': res.status_code,
            'data':  [],
            'message': 'Unable to fetch Lastest Recommendation...'
        }

        if res.status_code == requests.codes['ok']:
            resJSON = res.json()
            operationResult['isSuccess'] = True
            operationResult['data'] = resJSON['data']
            operationResult['message'] = resJSON['message']
        else:
            operationResult['isSuccess'] = False
            try:
                resJSON = res.json()
                operationResult['message'] = resJSON['message']
            except ValueError:
                operationResult['message'] = res.text
        return operationResult