#!/usr/bin/env python3

from Read_API import *
from LeagueClass import *

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

    def __str__ (self):
        player_info = (f'{self.first_name} {self.lastName} (#{self.primaryNumber}) {self.primaryPosition_name} \
Active:{self.rosterStatus} & is {self.currentAge} years old')

        return player_info

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

if __name__ == '__main__':
#     NHL_season = '20212022'
    NHL_season = '20222023'

    league = load_team_info (NHL_season) # league is a <class 'list'> of <class 'Team'>
    teams = [team.to_dict() for team in league] # build a list of dicts from your objects
    json_string = json.dumps ({'teams': teams}, indent=2)  # serialize the whole thing
#     print (json_string)
#     write_json (json_string, f'NHL_teams_{NHL_season}_info')
    
    for team in league:
        print (team)
        for player in team.roster:
            try:
                current_player = Player (player)
            except:
                print(f"{player} is not an active player")
            else:
                print (current_player)