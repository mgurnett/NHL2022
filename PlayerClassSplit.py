#!/usr/bin/env python3

from Read_API import *
from LeagueClass import *

class Player:
    ''' The Player class for a single player '''
    def __init__ (self, id, season):
        self.id = id
        self.season = season
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
        player_info = (f'{self.id} {self.first_name} {self.lastName} (#{self.primaryNumber}) {self.primaryPosition_name} \
Active:{self.rosterStatus} & is {self.currentAge} years old')
        player_stats = (f'\nHis stats are: {self.points} points (G-{self.goals} & A-{self.assists}) in {self.games} games')
        return player_info + player_stats

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
         
class Skater (Player):
''' The Player class for a single skater '''
    def __init__ (self, id, season):
        self.assists = 0
        self.goals = 0
        self.pim = 0
        self.shots = 0
        self.games = 0
        self.powerPlayGoals = 0
        self.powerPlayPoints = 0
        self.penaltyMinutes = 0
        self.shotPct = 0
        self.gameWinningGoals = 0
        self.overTimeGoals = 0
        self.shortHandedGoals = 0
        self.shortHandedPoints = 0
        self.plusMinus = 0
        self.points = 0
        
    def get_skater_stats():
        url = (f'people/{self.id}/stats?stats=statsSingleSeason&season={self.season}')
        data = read_API (url)
        data_stats = data['stats'][0]['splits'][0]['stat']
        self.assists = data_stats.get('assists')
        self.goals = data_stats.get('goals')
        self.pim = data_stats.get('pim')
        self.shots = data_stats.get('shots')
        self.games = data_stats.get('games')
        self.powerPlayGoals = data_stats.get('powerPlayGoals')
        self.powerPlayPoints = data_stats.get('powerPlayPoints')
        self.penaltyMinutes = data_stats.get('penaltyMinutes')
        self.shotPct = data_stats.get('shotPct')
        self.gameWinningGoals = data_stats.get('gameWinningGoals')
        self.overTimeGoals = data_stats.get('overTimeGoals')
        self.shortHandedGoals = data_stats.get('shortHandedGoals')
        self.shortHandedPoints = data_stats.get('shortHandedPoints')
        self.plusMinus = data_stats.get('plusMinus')
        self.points = data_stats.get('points')

class Goalie (Player):
    pass

if __name__ == '__main__':
    NHL_season = '20212022'
#     NHL_season = '20222023'
    '''
    league = load_team_info (NHL_season) # league is a <class 'list'> of <class 'Team'>
    teams = [team.to_dict() for team in league] # build a list of dicts from your objects
    json_string = json.dumps ({'teams': teams}, indent=2)  # serialize the whole thing
#     print (json_string)
#     write_json (json_string, f'NHL_teams_{NHL_season}_info')
    '''
# gets every player from every team
    '''  
    for team in league:
        print (team)
        for player in team.roster:
            try:
                current_player = Player (player)
            except:
                print(f"{player} is not an active player")
            else:
                print (current_player)'''
            
            
# gets every player from one team
    
    current_team = Team (22, NHL_season)
    for player in current_team.roster:
        try:
            current_player = Player (player, NHL_season)
        except:
            print(f"{player} is not an active player")
        else:
            print (current_player)