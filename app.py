import flask
from flask import Flask, request
import json
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return flask.render_template('index.html')

@app.route('/data', methods=['GET', 'POST'])
def get():
    apiKey = 'RGAPI-8edf16af-d2b5-4fff-ab58-ffcad9d6e239'
    summonerName = ''

    if request.method == 'GET':
        return flask.render_template('summoner_search.html')
    elif request.method == 'POST':
        summonerName = request.form['summoner_name']
        url = f'https://kr.api.riotgames.com/lol/summoner/v4/summoners/by-name/{summonerName}?api_key={apiKey}'
        summonerInfo = json.loads(requests.get(url).text)
        return flask.render_template('summoner_info.html', data=summonerInfo)

    # https://kr.api.riotgames.com/lol/summoner/v4/summoners/by-name/Colleen

if __name__ == '__main__':
    app.run()