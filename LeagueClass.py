#!/usr/bin/env python3

''' So this works for writting this to files, but is not correct.  The data that leagues gets is not accesable.'''

# import pandas as pd
from Read_API import *
from json_write import *

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
#         self.team_stats ()
#         self.get_roster ()

    def __str__ (self):
        team_info = (f'{self.name} of the {self.division} who play in {self.venue} in the {self.season} season.\n')
        team_stats = (f'They have have played {self.games_played} games with {self.win} wins and {self.loss} \
                        losses with {self.otloss} OT losses for {self.points} points\n')
#         return (team_info + team_stats)
        return (team_info)
        
class AllTeams ():
    ''' The League class for all teams '''
    def __init__ (self, TeamObjects):
        self.teams = list (TeamObjects)
        
    def __str__ (self):
        for x in self.teams:
            print (x)
    
def load_team_info (season):
    leag = []
    team_list = []
    url = (f'teams?season={season}')
    packages_json = read_API (url)
    for index in range (len(packages_json['teams'])):
        team_id = packages_json['teams'][index]['id']
        current_team = Team (team_id, season)
        current_team.name = packages_json['teams'][index]['name']
        current_team.abbreviation = packages_json['teams'][index]['abbreviation']
        current_team.teamName = packages_json['teams'][index]['teamName']
        current_team.locationName = packages_json['teams'][index]['locationName']
        current_team.shortName = packages_json['teams'][index]['shortName']
        current_team.division = packages_json['teams'][index]['division']['name']
        current_team.venue = packages_json['teams'][index]['venue']['name']
        team_list.append (current_team)
    leag = AllTeams (team_list)
    return (leag)
        
def update_team_stats (leag, season):

    for team in leag.teams:
#         url = (f'teams/{team.id}?expand=team.stats&season={season}')  team stats
        url = (f'teams/{team.id}/stats?season={season}')
        print (url)
        team_json = read_API (url)
        print (team.name)
        packages_str = json.dumps (team_json['stats'][0]['splits'][0]['stat'], indent =2)
        print (packages_str)
        print (str(packages_str['gamesPlayed']))
        team.games_played = int(packages_str['gamesPlayed'])
        team.points = team_json['stats']['splits']['stat']['pts']
        team.win = team_json['stats'][0]['splits'][0]['stat']['wins']
        team.loss = team_json['stats'][0]['splits'][0]['stat']['losses']
        team.otloss = team_json['stats'][0]['splits'][0]['stat']['ot']
        team.point_percent = team_json['stats'][0]['splits'][0]['stat']['ptPctg']
        team.goal_for = team_json['stats'][0]['splits'][0]['stat']['goalsPerGame']
        team.goal_against = team_json['stats'][0]['splits'][0]['stat']['goalsAgainstPerGame']
    return (leag)
               
if __name__ == '__main__':

    NHL_season = '20212022'

    league = load_team_info (NHL_season)

    league = update_team_stats (league, NHL_season)
    print (league)
    
    
#     json_league = league.to_json ()
#     write_json (json_league, "team_info")