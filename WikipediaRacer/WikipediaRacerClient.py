from flask import Flask, jsonify, request
from matplotlib.cbook import print_cycles
import requests

app = Flask(__name__)

hostIP = ''
myUser = ''


@app.route('/playerName', methods=['POST'])
def setPlayer():
    global myUser
    if myUser == '':
        #params = request.get_json()
        myUser = request.args.get('player')
    else:
        print('Warning, username already set!')
        #params = request.get_json()
        myUser = request.args.get('player')
    print('new username set to', myUser)
    return 'got name'


@app.route('/setHostIP', methods=['POST'])
def setHostIP():
    global hostIP
    if hostIP == '':
        #params = request.get_json()
        hostIP = request.args.get('ip')
        r = requests.post('http://' + hostIP + '/addPlayer', params={'player': myUser})
        if r.status_code == 200:
            print('connected to ', hostIP)
        return 'got IP'
    else: print('Warning, already in a lobby!')


@app.route('/acceptUrl', methods=['POST'])
def acceptUrl():
    #params = request.get_json()
    url = request.args.get('url')
    print('Recieved url:', url, ' sending to host')
    r = requests.post('http://' + hostIP + '/sendUrl', params={'url': url, 'player': myUser})
    if r.status_code == 200:
        print('yea it worked pog')
    return ''
