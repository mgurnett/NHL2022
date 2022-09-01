from flask import Flask
from PlayerClass import *

app = Flask (__name__)

@app.route ('/')
def index():
    return 'Hello World'

@app.route ('/player')
def player():
    url = 'teams/22?season=20212022'
    packages_json = read_API (url)
    current_player = Player (8480802)

    return str(current_player)

if __name__ == '__main__':

