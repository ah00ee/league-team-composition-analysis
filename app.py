import flask
from flask import Flask, request, url_for
import json
import requests

app = Flask(__name__)
'''
@app.route('/')
def home():
    return flask.render_template('index.html')
'''
@app.route('/')
def search():
    return flask.render_template('summoner_search.html')

@app.route('/data', methods=['GET'])
def get():
    summonerName = request.args.get('summoner_name')
    apiKey = 'Your Riot API KEY'
    url = f'https://kr.api.riotgames.com/lol/summoner/v4/summoners/by-name/{summonerName}?api_key={apiKey}'
    summonerInfo = json.loads(requests.get(url).text)

    return flask.render_template('summoner_info.html', data=summonerInfo)    

if __name__ == '__main__':
    app.run()
