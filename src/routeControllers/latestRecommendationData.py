from typing import List
from flask import Blueprint, render_template
from src.config.appConfig import getJsonConfig
from src.repos.fetchRecommendation import RecommendationSummaryRepo
from src.services.latestRecommendationFetcher import LatestRecommendationFetcher

latestRecommendationPage = Blueprint('latestRecommendation', __name__,
                                template_folder='templates')

@latestRecommendationPage.route('/', methods=['GET', 'POST'])
# @role_required('code_book_editor')
def displayLatestRecommendation():
    # get application config
    dbConfig = getJsonConfig()

    # get the instance of min_wise demand storage repository
    # latestRecommendationSummaryRepo= RecommendationSummaryRepo(dbConfig.appDbConnStr)
    # in case of post request, fetch 
    # if request.method == 'POST':
    latestRecommendationSummaryRepo = LatestRecommendationFetcher(dbConfig.latestatestRecommendationFetchUrl)
    
    # fetch scada sem data from db via the repository instance of ith state
    resp = latestRecommendationSummaryRepo.fetchLatestRecommendation()

    data = resp['data']

    return render_template('Recommendations/test.html.j2', data=data)
    # in case of get request just return the html template
    # return render_template('Recommendations/latestRecommendation.html.j2')

# @latestRecommendationPage.route('/', methods=['GET', 'POST'])
# # @role_required('code_book_editor')
# def displayInformationalRecommendation():
#     # get application config
#     dbConfig = getJsonConfig()

#     # get the instance of min_wise demand storage repository
#     # latestRecommendationSummaryRepo= RecommendationSummaryRepo(dbConfig.appDbConnStr)
#     # in case of post request, fetch 
#     # if request.method == 'POST':
#     latestRecommendationSummaryRepo = LatestRecommendationFetcher(dbConfig.latestatestRecommendationFetchUrl)
    
#     # fetch scada sem data from db via the repository instance of ith state
#     resp = latestRecommendationSummaryRepo.fetchLatestRecommendation()

#     data = resp['data']

#     return render_template('Recommendations/test.html.j2', data=data)
#     # in case of get request just return the html template
#     # return render_template('Recommendations/latestRecommendation.html.j2')

@latestRecommendationPage.route('/', methods=['GET', 'POST'])
# @role_required('code_book_editor')
def plot():
    # get application config
    dbConfig = getJsonConfig()
    appDbConnStr = dbConfig.appDbConnStr


    # get the instance of min_wise demand storage repository
    latestRecommendationSummaryRepo= RecommendationSummaryRepo(appDbConnStr)
    # in case of post request, fetch 
    # if request.method == 'POST':
    
    # fetch scada sem data from db via the repository instance of ith state
    data = latestRecommendationSummaryRepo.fetchLatestRecommendation()

    return render_template('Recommendations/plot.html.j2', data=data, subStation=subStation)
    # in case of get request just return the html template
    # return render_template('Recommendations/latestRecommendation.html.j2')
