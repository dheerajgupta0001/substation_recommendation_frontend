'''
This is the web server that acts as a service that creates scada sem data
'''
# from flask import Markup
from flask import Flask, request, jsonify, render_template
from waitress import serve
from src.config.appConfig import loadJsonConfig
from src.routeControllers.latestRecommendationData import latestRecommendationPage
from src.routeControllers.latestRecommendationApi import latestRecommendationApiPage

# get application config
appConfig = loadJsonConfig()

app = Flask(__name__)

# Set the secret key to some random bytes
app.secret_key = appConfig.flaskSecret

@app.route('/')
def hello():
    return render_template('home.html.j2')

app.register_blueprint(latestRecommendationPage, url_prefix='/latestRecommendation')
app.register_blueprint(latestRecommendationApiPage, url_prefix='/fetchLatestRecommendation')

if __name__ == '__main__':
    serverMode: str = appConfig.mode
    if serverMode.lower() == 'p':
        app.run(host="0.0.0.0", port=int(appConfig.flask_port), debug=True)
    else:
        serve(app, host='0.0.0.0', port=int(appConfig.flask_port), threads=1)
