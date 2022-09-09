#!/usr/bin/env python3

# import pandas as pd
from Read_API import *
# from PlayerClass import *
# from TeamClass import *
from json_write import *

class League ():
    ''' The League class for all teams '''
    def __init__ (self):
        self.season = '20212022'
        self.teams = []
        self.get_team_ids ()
        
    def print_team_ids (self):
        self.teams.append(id) 
        for index in self.teams:
            print (index)

    def get_team_ids (self):
        url = (f'teams?season={self.season}')
        packages_json = read_API (url)
        for index in range (len(packages_json['teams'])):
            id = packages_json['teams'][index]['id']
            self.teams.append(id) 

    def to_json(self):
        return json.dumps(self, default=lambda obj: self.__dict__, indent=4)

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
    json_league = league.to_json ()
    print (json_league)
    write_json (json_league, "team_ids")