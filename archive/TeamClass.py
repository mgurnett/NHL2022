#!/usr/bin/env python3

from michael_debug import *
from Read_API import *  # import requests is in Read_API
from LeagueClass import *
from PlayerClass import *

NHL_season = '20212022'

class Team:
    ''' The Team class for a single team '''
    def __init__ (self, id, season):
        self.id = id
        self.season = NHL_season
        self.name = ""
        self.teamName = ""
        self.abbreviation = ""
        self.locationName = ""
        self.shortName = ""
        self.division = ""
        self.conference = ""
        self.venue = ""
        self.win = 0
        self.loss = 0
        self.otloss = 0
        self.points = 0
        self.games_played = 0
        self.point_percent = 0
        self.goal_for = 0
        self.goal_against = 0
        self.roster = []
        self.team_stats ()
#         self.get_roster ()

    def __str__ (self):
        team_info = (f'{self.name} of the {self.division} who play in {self.venue} and have {self.points} points in the {self.season} season.\n')
        team_stats = (f'They have have played {self.games_played} games with {self.win} wins and {self.loss} losses with {self.otloss} OT losses\n')
        return (team_info + team_stats)
   
    def team_stats (self):
        url = (f'teams/{self.id}?season={self.season}')  #team info
        team_json = read_API (url)
        self.name = team_json['teams'][0]['name'] # better way to do is to get all the data in a hash and then pull the data out.
        self.division = team_json['teams'][0]['division']['name']
        self.venue = team_json['teams'][0]['venue']['name']
        
        url = (f'teams/{self.id}/stats?season={self.season}')  #team stats
        team_json = read_API (url)
        self.games_played = team_json['stats'][0]['splits'][0]['stat']['gamesPlayed']
        self.points = team_json['stats'][0]['splits'][0]['stat']['pts']
        self.win = team_json['stats'][0]['splits'][0]['stat']['wins']
        self.loss = team_json['stats'][0]['splits'][0]['stat']['losses']
        self.otloss = team_json['stats'][0]['splits'][0]['stat']['ot']
        self.point_percent = team_json['stats'][0]['splits'][0]['stat']['ptPctg']
        self.goal_for = team_json['stats'][0]['splits'][0]['stat']['goalsPerGame']
        self.goal_against = team_json['stats'][0]['splits'][0]['stat']['goalsAgainstPerGame']

def get_roster(team_id):
    roster = []
    active_roster = []
    url = (f'teams/{str(team_id)}/roster')
    data = read_API (url)
    roster_df = pd.json_normalize(data, ['roster'],  errors='ignore')
    # ; print (roster_df['person.id'])
    roster.append(roster_df['person.id'])
    for r in roster_df['person.id']:
        active_roster.append(r)
        current_player = Player (r)
#             print (current_player)
#         print (active_roster)
    return active_roster
    
def get_teams (season):
    team_list = [] # this is a list
#     url = 'teams'
    url = (f'teams?season={season}')
    packages_json = read_API (url)
    for index in range (len(packages_json['teams'])):
        team_id = packages_json['teams'][index]['id']
        current_team = Team (team_id, season)
        team_list.append (current_team)
    return (team_list)
    
if __name__ == '__main__':
    league = get_teams (NHL_season)  #league is the full iteration of Class teams as a list
    for team in league:
        print (team)
        frozen = jsonpickle.encode(team)
        print (frozen)
