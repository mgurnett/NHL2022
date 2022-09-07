#!/usr/bin/env python3

import json
import requests
import pandas as pd
from Read_API import *
from PlayerClass import *

class Team:
    ''' The Team class for a single team '''
    def __init__ (self, id):
        self.id = id
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
        return (f'{self.name} of the {self.division} who play in {self.venue} and have played {self.games_played} games and have {self.points} points')
   
    def team_stats (self):
        url = (f'teams/{self.id}?season=20222023')  #team info
        team_json = read_API (url)
        self.name = team_json['teams'][0]['name'] # better way to do is to get all the data in a hash and then pull the data out.
        self.division = team_json['teams'][0]['division']['name']
        self.venue = team_json['teams'][0]['venue']['name']
        
        url = (f'teams/{self.id}/stats?season=20222023')  #team stats
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
    
def get_teams ():
    team_list = [] # this is a list
#     url = 'teams'
    url = 'teams?season=20222023'
    packages_json = read_API (url)
    for index in range (len(packages_json['teams'])):
        team_id = packages_json['teams'][index]['id']
        current_team = Team (team_id)
        team_list.append (current_team)
    return (team_list)
    
if __name__ == '__main__':
    # url = 'schedule?date=2021-03-27'
#     url = 'teams/22?season=20212022'
#     packages_json = read_API (url)
#     current_team = Team (22)
#     current_team.roster = Team.get_roster
#     print (current_team.roster)
#     print (current_team.goal_for)
    league = get_teams ()  #league is the full iteration of Class teams.
    for team in league:
        print (team)
