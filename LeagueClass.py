#!/usr/bin/env python3

# import pandas as pd
from Read_API import *
from json_write import *

class League ():
    ''' The League class for all teams '''
    def __init__ (self, season):
        self.season = season
        self.teams = []
        self.get_teams ()
        
    def get_teams (self):
        url = (f'teams?season={self.season}')
        packages_json = read_API (url)
        for index in range (len(packages_json['teams'])):
            id = {'id': packages_json['teams'][index]['id'],
                  'name': packages_json['teams'][index]['name'],
                  'abbreviation': packages_json['teams'][index]['abbreviation'],
                  'teamName': packages_json['teams'][index]['teamName'],
                  'locationName': packages_json['teams'][index]['locationName'],
                  'shortName': packages_json['teams'][index]['shortName'],
                  'division': packages_json['teams'][index]['division']['name'],
                  'venue': packages_json['teams'][index]['venue']['name']
                  }
            self.teams.append(id)

    def to_json(self):
        return json.dumps(self, default=lambda obj: self.__dict__, indent=4)

    def print_teams (self):
        for team in self.teams:
            print (f'{team.name} of the {self.division} who play in {self.venue}')
               
if __name__ == '__main__':
    league = League ('20202021')
    json_league = league.to_json ()
    write_json (json_league, "team_info")