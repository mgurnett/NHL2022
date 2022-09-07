#!/usr/bin/env python3

import json
import requests
import pandas as pd
from Read_API import *

def get_league ():
    team_list = [] # this is a list
#     url = 'teams'
    url = 'teams?season=20222023'
    packages_json = read_API (url)
    for index in range (len(packages_json['teams'])):
        team_id = packages_json['teams'][index]['id']
        current_team = Team (team_id)
        current_team.name = packages_json['teams'][index]['name']
        current_team.abbreviation = packages_json['teams'][index]['abbreviation']
        current_team.teamName = packages_json['teams'][index]['teamName']
        current_team.locationName = packages_json['teams'][index]['locationName']
        current_team.shortName = packages_json['teams'][index]['shortName']
        current_team.division = packages_json['teams'][index]['division']['name']
        current_team.venue = packages_json['teams'][index]['venue']['name']
#         current_team.roster = Team.get_roster (team_id)
#         team_list.append (current_team)
        print (current_team)
    return (team_list)

    def __str__ (self):
        return (f'{self.name} of the {self.division} who play in {self.venue} and have played {self.games_played} games and have {self.points} points')

        

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
        self.get_roster ()

    def __str__ (self):
        return (f'{self.name} of the {self.division} who play in {self.venue} and have played {self.games_played} games and have {self.points} points')

        
    def team_stats (self):
        url = (f'teams/{self.id}?season=20212022')  #team info
        team_json = read_API (url)
        self.name = team_json['teams'][0]['name'] # better way to do is to get all the data in a hash and then pull the data out.
        # def load_player_data in PlayerClass
        self.division = team_json['teams'][0]['division']['name']
        self.venue = team_json['teams'][0]['venue']['name']
        
        url = (f'teams/{self.id}/stats?season=20212022')  #team stats
        team_json = read_API (url)
        self.games_played = team_json['stats'][0]['splits'][0]['stat']['gamesPlayed']
        self.points = team_json['stats'][0]['splits'][0]['stat']['pts']
        self.win = team_json['stats'][0]['splits'][0]['stat']['wins']
        self.loss = team_json['stats'][0]['splits'][0]['stat']['losses']
        self.otloss = team_json['stats'][0]['splits'][0]['stat']['ot']
        self.point_percent = team_json['stats'][0]['splits'][0]['stat']['ptPctg']
        self.goal_for = team_json['stats'][0]['splits'][0]['stat']['goalsPerGame']
        self.goal_against = team_json['stats'][0]['splits'][0]['stat']['goalsAgainstPerGame']
        
    def get_roster(self):
        roster = []
        active_roster = []
        url = (f'teams/{str(self.id)}/roster')
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
    
class Player:
    ''' The Player class for a single player '''
    def __init__ (self, id):
        self.id = id
        self.first_name = ''
        self.lastName = ''
        self.primaryNumber = ''
        self.currentAge = ''
        self.nationality = ''
        self.alternateCaptain = ''
        self.captain = ''
        self.rosterStatus = ''
        self.currentTeam = ''
        self.primaryPosition_name = ''
        self.birthDate = ''
        self.birthCountry = ''
        self.nationality = ''
        self.rookie = ''
        self.shootsCatches = ''
        self.load_player_data()

    def load_player_data (self):
        url = (f'people/{str(self.id)}')
        data = read_API (url)
        data_people = data['people'][0]
        self.first_name = data_people.get('firstName')
        self.lastName = data_people.get('lastName')
        self.primaryNumber = data_people.get('primaryNumber')
        self.currentAge = data_people.get('currentAge')
        self.nationality = data_people.get('nationality')
        self.alternateCaptain = data_people.get('alternateCaptain')
        self.captain = data_people.get('captain')
        self.rosterStatus = data_people.get('rosterStatus')
        self.currentTeam = data_people.get('currentTeam').get('name')
        self.primaryPosition_name = data_people.get('primaryPosition').get('name')
        self.birthDate = data_people.get('birthDate')
        self.birthCountry = data_people.get('birthCountry')
        self.nationality = data_people.get('nationality')
        self.rookie = data_people.get('rookie')
        self.shootsCatches = data_people.get('shootsCatches')