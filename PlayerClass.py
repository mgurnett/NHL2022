#!/usr/bin/env python3

import json
import requests
from Read_API import *

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
        return (f'{self.first_name} {self.lastName} (#{self.primaryNumber}) {self.primaryPosition_name} Active:{self.rosterStatus} & is {self.currentAge} years old')

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

    # url = 'schedule?date=2021-03-27'
    url = 'teams/22?season=20212022'
    packages_json = read_API (url)
    current_player = Player (8480802)
    print (current_player)
#     
#     url = 'teams/22/stats?season=20212022'
#     packages_json = read_API (url)
#     packages_str = json.dumps (packages_json['stats'][0]['splits'][0], indent =2)
# #     packages_str = json.dumps (packages_json['teams'][0]['name'], indent =2)
#     print (packages_str)