#!/usr/bin/env python3

import json
import requests
import pandas as pd
from Read_API import *
from PlayerClass import *

https://statsapi.web.nhl.com/api/v1/schedule?teamId=22&startDate=2022-09-25&endDate=2022-10-07

class Game:
    ''' The Game class for a single game '''
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

if __name__ == '__main__':
    
