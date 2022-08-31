#!/usr/bin/env python3

import json
import requests
import pandas as pd
from Read_API import *

class Game:
    ''' The Game class for a single game '''
    def __init__ (self, id):
        self.id = id
        self.status = ''
        self.date = ''
        self.home = ''
        self.away = ''
        self.home_object = ''
        self.away_object = ''
        self.home_score = 0
        self.away_score = 0
        self.home_point = 0
        self.away_point = 0

    def __str__ (self):
        if self.status == 'Final':
            return (f'{self.date} ({self.id}) {self.home} was home to the {self.away}.  The score was {self.home_score} - {self.away_score} {self.status}')
        elif self.status in ('In Progress', 'Pre-Game'):
            return (f'{self.date} ({self.id}) {self.home} are home to the {self.away}.  The score is {self.home_score} - {self.away_score} {self.status}')
        else:
            return (f'{self.date} ({self.id}) {self.home} will be home to the {self.away}.  {self.status}')
        
        
if __name__ == '__main__':
    dates = []
    games = []
    url = "schedule?teamId=22&startDate=2022-09-25&endDate=2022-10-07"
    schedule_json = read_API(url)
    numb_of_games = json.dumps (schedule_json['totalItems'])
    for game_numb in range (int(numb_of_games)):
        current_date = json.dumps (schedule_json['dates'][game_numb]['date'])
        current_game = Game (game_numb)
        print (current_game)
        print (game_numb, " - ", current_date)
        dates.append (current_date)
        games.append (gurrnet_game)
    print (dates)
