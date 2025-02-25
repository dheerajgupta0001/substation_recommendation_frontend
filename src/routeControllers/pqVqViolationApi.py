from typing import List
from flask import Blueprint, render_template
from src.config.appConfig import getAppConfig
from src.repos.fetchPqVqViolation import PqVqViolationSummaryRepo
from src.services.pqVqViolationFetcher import PqVqViolationFetcher
from src.security.decorators import roles_required
from flask import Flask, request, jsonify

from src.typeDefs.pqVqViolationSummary import IPqVqViolationSummary

pqVqViolationApiPage = Blueprint('pqVqViolationApi', __name__,
                                template_folder='templates')

@pqVqViolationApiPage.route('/', methods=['GET'])
@roles_required(['recommendation_app_user'])
def fetchPqVqViolation():
    # get application config
    dbConfig = getAppConfig()
    data = {}
    try:
        # Get date parameters from request
        start_date = request.args.get('startDate', None)
        end_date = request.args.get('endDate', None)
        # get PQ VQ violation Message
        pqVqViolationSummaryRepo = PqVqViolationSummaryRepo(dbConfig.appDbConnStr)
        data1: List[IPqVqViolationSummary] = pqVqViolationSummaryRepo.fetchPqVqViolation(start_date, end_date)

        data['data1'] = data1

        if data:
            return jsonify({'message': 'Success!!!', 'data': data})
        else:
            return jsonify({'message': 'PQ VQ Violation fetch unsuccessfull'}), 500
    except Exception as ex:
        return jsonify({'message': 'some error occured...'}), 400
