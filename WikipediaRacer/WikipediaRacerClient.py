from flask import Flask, jsonify, request
import time

app = Flask(__name__)

hostIP = ''

@app.route('/acceptUrl', methods=['POST'])
def acceptUrl():
    pass