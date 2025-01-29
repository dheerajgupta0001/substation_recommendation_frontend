'''
This is the web server that acts as a service that creates scada sem data
'''
# from flask import Markup
from flask import Flask, request, jsonify, render_template, request, redirect, url_for, flash, sessions
from src.routeControllers.oauth import login_manager, oauthPage, initOauthClient
from src.security.errorHandlers import page_forbidden, page_not_found, page_unauthorized
from waitress import serve
from src.config.appConfig import loadAppConfig
from src.routeControllers.latestRecommendationData import latestRecommendationPage
from src.routeControllers.latestRecommendationApi import latestRecommendationApiPage
import os
from src.security.decorators import role_required
from src.routeControllers.pqVqViolationData import pqVqViolationPage
from src.routeControllers.pqVqViolationApi import pqVqViolationApiPage

# get application config
appConfig = loadAppConfig()

initOauthClient()

# set this variable since we are currently not running this app on SSL
os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'

app = Flask(__name__)

# Set the secret key to some random bytes
app.secret_key = appConfig.flaskSecret

# User session management setup
login_manager.init_app(app)

@app.route('/')
def index():
    return render_template('home.html.j2')

app.register_error_handler(401, page_unauthorized)
app.register_error_handler(403, page_forbidden)
app.register_error_handler(404, page_not_found)
app.register_blueprint(oauthPage, url_prefix='/oauth')
app.register_blueprint(latestRecommendationPage, url_prefix='/latestRecommendation')
app.register_blueprint(latestRecommendationApiPage, url_prefix='/fetchLatestRecommendation')
app.register_blueprint(pqVqViolationPage, url_prefix='/pqVqViolation')
app.register_blueprint(pqVqViolationApiPage, url_prefix='/fetchPqVqViolation')

if __name__ == '__main__':
    serverMode: str = appConfig.mode
    if serverMode.lower() == 'p':
        app.run(host="0.0.0.0", port=int(appConfig.flask_port), debug=True)
    else:
        serve(app, host='0.0.0.0', port=int(appConfig.flask_port), threads=1)
