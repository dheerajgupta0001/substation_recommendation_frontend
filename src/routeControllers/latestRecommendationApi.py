from typing import List
from flask import Blueprint, render_template
from src.config.appConfig import getJsonConfig
from src.repos.fetchRecommendation import RecommendationSummaryRepo
from src.services.latestRecommendationFetcher import LatestRecommendationFetcher
from flask import Flask, request, jsonify

from src.typeDefs.latestRecommendationSummary import ILatestRecommendationSummary

latestRecommendationApiPage = Blueprint('latestRecommendationApi', __name__,
                                template_folder='templates')

@latestRecommendationApiPage.route('/', methods=['GET'])
def fetchLatestRecommendation():
    # get application config
    dbConfig = getJsonConfig()
    data = {}
    try:
        # get iegc violation messages
        latestRecommendationSummaryRepo = RecommendationSummaryRepo(dbConfig.appDbConnStr)
        data1: List[ILatestRecommendationSummary] = latestRecommendationSummaryRepo.fetchLatestRecommendation(True)

        data2: List[ILatestRecommendationSummary] = latestRecommendationSummaryRepo.fetchLatestRecommendation(False)

        data['data1'] = data1
        data['data2'] = data2

        if data:
            return jsonify({'message': 'Success!!!', 'data': data})
        else:
            return jsonify({'message': 'Latest Recommendation fetch unsuccessfull'}), 500
    except Exception as ex:
        return jsonify({'message': 'some error occured...'}), 400
