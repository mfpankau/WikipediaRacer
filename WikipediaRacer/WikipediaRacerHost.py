from flask import Flask, jsonify, request
import time

app = Flask(__name__)

players = []
websitesViewed = {}

def addNewWebsite(player, url):
    if player in players:
        if not websitesViewed[player][len(websitesViewed[player]) - 1] == url:
            websitesViewed[player].append(url)
            print(player, 'has visited site', url)
    print('at least i ran')


@app.route('/addPlayer', methods=['POST'])
def addPlayer():
    player = request.args.get('player')
    #player = params['player']
    if player not in players:
        players.append(player)
        print('new player joined: ', player)
    return ''

@app.route('/removePlayer', methods=['POST'])
def removePlayer():
    player = request.args.get('player')
    if player in players:
        players.remove(player)
        print('player left: ', player)
    return ''

@app.route('/sendUrl', methods=['POST'])
def addUrl():
    #params = request.get_json()
    url = request.args.get('url')
    player = request.args.get('player')
    addNewWebsite(player=player, url=url)
    return ''




