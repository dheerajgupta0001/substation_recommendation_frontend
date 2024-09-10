from typing import List
from flask import Blueprint, render_template, request
from src.config.appConfig import getJsonConfig
from src.repos.fetchRecommendation import RecommendationSummaryRepo
from src.services.latestRecommendationFetcher import LatestRecommendationFetcher
import json

latestRecommendationPage = Blueprint('latestRecommendation', __name__,
                                     template_folder='templates')


@latestRecommendationPage.route('/', methods=['GET', 'POST'])
# @role_required('code_book_editor')
def displayLatestRecommendation():

    if request.method == 'POST':

        return render_template('Recommendations/plotRecommendationById.html.j2')

    # dbConfig = getJsonConfig()
    # latestRecommendationSummaryRepo = LatestRecommendationFetcher(dbConfig.latestatestRecommendationFetchUrl)
    # resp = latestRecommendationSummaryRepo.fetchLatestRecommendation()
    # data = resp['data']
    # return render_template('Recommendations/latestRecommendation.html.j2', data=data)

    return render_template('Recommendations/latestRecommendation.html.j2')


@latestRecommendationPage.route('/selected-data', methods=['POST'])
def selected_data():
    # get application config
    dbConfig = getJsonConfig()
    appDbConnStr = dbConfig.appDbConnStr

    selected_id = int(json.loads(request.form.get('selectedData'))['id'])
    substation_name = json.loads(request.form.get('selectedData'))[
        'substation_name']
    recommendation = json.loads(request.form.get('selectedData'))[
        'recommendation']

    # get the instance of latest recommendation repository
    latestRecommendationSummaryRepo = RecommendationSummaryRepo(appDbConnStr)
    resp = latestRecommendationSummaryRepo.fetchRecommendationById(selected_id)

    voltage_str = resp['voltage_str']

    voltage_list = voltage_str.split(',')

    voltage_list = [float(x) for x in voltage_list]

    # Redirect back to the main page
    return render_template('Recommendations/plotRecommendationById.html.j2', substation_name=substation_name, data=voltage_list, recommendation=recommendation)
