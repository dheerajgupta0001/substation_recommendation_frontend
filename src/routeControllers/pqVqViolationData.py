from typing import List
from flask import Blueprint, render_template, request
from src.security.decorators import roles_required
import json

pqVqViolationPage = Blueprint('pqVqViolation', __name__,
                                     template_folder='templates')


@pqVqViolationPage.route('/', methods=['GET', 'POST'])
@roles_required(['recommendation_app_user'])
def displayPqVqViolation():

    if request.method == 'POST':

        return render_template('PqVqViolation/pqVqViolation.html.j2')

    return render_template('PqVqViolation/pqVqViolation.html.j2')