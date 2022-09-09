#!/usr/bin/env python3

import jsonpickle # import json is in jsonpickle
# see http://jsonpickle.github.io/ for documentation
# import pandas as pd
from Read_API import *
# from PlayerClass import *
# from TeamClass import *

class League ():
    ''' The League class for all teams '''
    def __init__ (self):
        self.id = id
        self.name = ""
        self.teamName = ""
        self.abbreviation = ""
        self.locationName = ""
        self.shortName = ""
        self.division = ""
        self.conference = ""
        self.venue = ""
        self.teams = []
        self.teams = self.get_teams ()

    def get_teams (self):
        team_list = [] # this is a list
    #     url = 'teams'
        url = 'teams?season=20222023'
        packages_json = read_API (url)
        for index in range (len(packages_json['teams'])):
            self.id = packages_json['teams'][index]['id']
            self.name = packages_json['teams'][index]['name']
            self.abbreviation = packages_json['teams'][index]['abbreviation']
            self.teamName = packages_json['teams'][index]['teamName']
            self.locationName = packages_json['teams'][index]['locationName']
            self.shortName = packages_json['teams'][index]['shortName']
            self.division = packages_json['teams'][index]['division']['name']
            self.venue = packages_json['teams'][index]['venue']['name']
            team_list.append (self)
            print (self.name)
        return (team_list) 

def print_teams (team_list):
    for team in team_list:
        print (f'{self.name} of the {self.division} who play in {self.venue}')
               
        
if __name__ == '__main__':
    league = League ()
#     json_league = json.dumps(league)
#     print (json_league)
    frozen = jsonpickle.encode(league)
    print (frozen)
