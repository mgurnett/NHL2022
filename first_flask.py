from flask import Flask
from PlayerClass import *
from LeagueClass import *

NHL_season = '20212022'
app = Flask (__name__)

@app.route ('/')
def index():
    return 'Hello World'

@app.route ('/player')
def player():
    league = load_team_info (NHL_season)
    current_team = Team (22, NHL_season)
    print (current_team)
    for player in current_team.roster:
        try:
            current_player = Player (player, NHL_season)
        except:
            print(f"{player} is not an active player")
        else:
            return str(current_player)

@app.route ('/teams')
def teams():
    league = load_team_info (NHL_season) # league is a <class 'list'> of <class 'Team'>
    league = update_team_stats (league, NHL_season) # league is a <class 'list'> of <class 'Team'>
    teams = [team.to_dict() for team in league] # build a list of dicts from your objects
    json_string = json.dumps ({'teams': teams}, indent=2)  # serialize the whole thing
    return json_string

if __name__ == '__main__':
    pass