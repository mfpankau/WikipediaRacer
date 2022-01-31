from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

hostIP = ''
myUser = ''

def start():
    app.run(host='0.0.0.0', port='5000')


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
    return ''


@app.route('/setHostIP', methods=['POST'])
def setHostIP():
    global hostIP
    hostIP = request.args.get('ip')
    return ''


@app.route('/connect', methods=['POST'])
def connectToHost():
    if hostIP != '' and myUser != '':
        r = requests.post('http://' + hostIP + '/addPlayer', params={'player': myUser})
        if r.status_code == 200:
            print('connected to ', hostIP)
    return ''


@app.route('/acceptUrl', methods=['POST'])
def acceptUrl():
    #params = request.get_json()
    url = request.args.get('url')
    print('Recieved url:', url, ' sending to host')
    if url != '' and hostIP != '' and myUser != '':
        r = requests.post('http://' + hostIP + '/sendUrl', params={'url': url, 'player': myUser})
        if r.status_code == 200:
            print('yea it worked pog')
    return ''


if __name__ == '__main__':
    start()