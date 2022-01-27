from flask import Flask, jsonify, request
import time

app = Flask(__name__)

players = []
websitesViewed = {}

def addNewWebsite(player, url):
    if player in players:
        if not websitesViewed[len(websitesViewed[player]) - 1] == url:
            websitesViewed[player].append(url)


@app.route('/addPlayer', methods=['POST'])
def addPlayer():
    params = request.get_data().decode()
    player = params.replace('player=', '')
    if player not in players:
        players.append(player)
    pass

@app.route('/removePlayer', methods=['POST'])
def removePlayer():
    params = request.get_data().decode()
    player = params.replace('player=', '')
    if player in players:
        players.remove(player)
    pass

@app.route('sendUrl', methods=['POST'])
def addUrl():
    params = request.get_json()
    url = params['url']
    player = params['player']
    addNewWebsite(player=player, url=url)




