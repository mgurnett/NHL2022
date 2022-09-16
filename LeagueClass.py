#!/usr/bin/env python3

from michael_debug import debug_var
from json_write import *
from Read_API import *

class Team:
    ''' The Team class for a single team '''
    def __init__ (self, id, season):
        self.id = id
        self.season = season
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
        self.get_roster ()
#         self.team_stats ()

    def __str__ (self):
        team_info = (f'{self.name} of the {self.division} who play in {self.venue} in the {self.season} season.\n')
        team_stats = (f'They have have played {self.games_played} games with {self.win} wins and {self.loss} \
losses with {self.otloss} OT losses for {self.points} points\n')
        roster_print = str(self.roster)
        return (team_info + team_stats + roster_print)
#         return (team_info)

#https://stackoverflow.com/questions/50811101/convert-list-of-class-objects-into-json-in-python-or-django for help with this
    def to_dict(self):
            return {"id": self.id,
                    "name": self.name,
                    "season": self.season,
                    "teamName": self.teamName,
                    "abbreviation": self.abbreviation,
                    "locationName": self.locationName,
                    "shortName": self.shortName,
                    "division": self.division,
                    "conference": self.conference,
                    "venue": self.venue,
                    "win": self.win,
                    "loss": self.loss,
                    "otloss": self.otloss,
                    "points": self.points,
                    "games_played": self.games_played,
                    "point_percent": self.point_percent,
                    "goal_for": self.goal_for,
                    "goal_against": self.goal_against,
                    "roster": self.roster
                    }
        
    def get_roster (self):
        self.roster = []
        url = (f'teams/{self.id}?expand=team.roster&season={self.season}')
        roster_str = read_API (url)
    #     print (roster ['teams'][0]['roster']['roster'][0])
        for player in roster_str ['teams'][0]['roster']['roster']: 
            current_player = player ['person']['id']
            self.roster.append (current_player)
        return 
        
def load_team_info (season):
    leag = []
    url = (f'teams?season={season}')
    teams = read_API (url)
        
    for team in teams ['teams']:
        team_id = team ['id']
        current_team = Team (team_id, season)
        current_team.name = team ['name']
        current_team.abbreviation = team ['abbreviation']
        current_team.teamName = team ['teamName']
        current_team.locationName = team ['locationName']
        current_team.shortName = team ['shortName']
        current_team.division = team ['division']['name']
        current_team.venue = team ['venue']['name']
        leag.append (current_team)
#         print (current_team, type(current_team))
    return (leag)
        
def update_team_stats (leag, season):

    for team in leag:
#         url = (f'teams/{team.id}?expand=team.stats&season={season}')  team stats

        url = (f'teams/{int(team.id)}/stats?season={season}')
        team_json = read_API (url)
        
        team.games_played = team_json['stats'][0]['splits'][0]['stat']['gamesPlayed']
        team.points = team_json['stats'][0]['splits'][0]['stat']['pts']
        team.win = team_json['stats'][0]['splits'][0]['stat']['wins']
        team.loss = team_json['stats'][0]['splits'][0]['stat']['losses']
        team.otloss = team_json['stats'][0]['splits'][0]['stat']['ot']
        team.point_percent = team_json['stats'][0]['splits'][0]['stat']['ptPctg']
        team.goal_for = team_json['stats'][0]['splits'][0]['stat']['goalsPerGame']
        team.goal_against = team_json['stats'][0]['splits'][0]['stat']['goalsAgainstPerGame']
#         print (team)
    return (leag)
               
if __name__ == '__main__':
    NHL_season = '20212022'

    league = load_team_info (NHL_season) # league is a <class 'list'> of <class 'Team'>
    teams = [team.to_dict() for team in league] # build a list of dicts from your objects
    json_string = json.dumps ({'teams': teams}, indent=2)  # serialize the whole thing
#     print (json_string)
    write_json (json_string, f'NHL_teams_{NHL_season}_info')
    
    league = update_team_stats (league, NHL_season) # league is a <class 'list'> of <class 'Team'>
    teams = [team.to_dict() for team in league] # build a list of dicts from your objects
    json_string = json.dumps ({'teams': teams}, indent=2)  # serialize the whole thing
#     print (json_string)
    write_json (json_string, f'NHL_teams_{NHL_season}_stats')
    
    for team in league:
        print (team)