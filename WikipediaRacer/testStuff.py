import requests

def testStuff(str):
    if str == 'URL':
        requests.post('http://localhost:5000/acceptUrl', params={'url':'idk.com'})
    elif str == 'Name':
        user = input('idk type smthn:')
        requests.post('http://localhost:5000/playerName', params={'player':user})
    elif str == 'IP':
        ip = input('what is the hosts ip(xxx.xxx.xxx.xxx:pppp): ')
        requests.post('http://127.0.0.1:5000/setHostIP', params={'ip':ip})

while True:
    str = input('command: ')
    testStuff(str)