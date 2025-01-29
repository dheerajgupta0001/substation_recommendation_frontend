import requests
import datetime as dt
from src.typeDefs.pqVqViolationFetchResp import IPqVqViolationFetchResp

class PqVqViolationFetcher():
    pqVqViolationFetchUrl = ''

    def __init__(self, pqVqViolationFetchUrl):
        self.pqVqViolationFetchUrl = pqVqViolationFetchUrl

    def fetchPqVqViolation(self) -> IPqVqViolationFetchResp:
        """_summary_

        Returns:
            IPqVqViolationFetchResp: _description_
        """
        res = requests.get(self.pqVqViolationFetchUrl)

        operationResult: IPqVqViolationFetchResp = {
            "isSuccess": False,
            'status': res.status_code,
            'data':  [],
            'message': 'Unable to fetch PQ VQ Violation...'
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