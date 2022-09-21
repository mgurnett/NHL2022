#!/usr/bin/env python3

from michael_debug import debug_var
from Read_API import *
import pandas as pd

NHL_season = '20212022'

class Team ():
    def __init__ (self, id, season):
        self.id = id
        self.season = season
        self.sub_url = f'teams/{self.id}?expand=team.roster&season={self.season}'
        self.get_data ()
    
    def get_data (self):
        data = read_API (self.sub_url)

        df_nested_list = pd.json_normalize(data, record_path =['teams'])
        self.team_pd = df_nested_list.drop('roster.roster', axis=1)
        
    @staticmethod  
    def load_team_info (season):
        leag = []
        url = (f'teams?season={season}')
        teams = read_API (url)
        for team in teams ['teams']:
            team_id = team ['id']
            leag.append (team_id)
        return (leag)

if __name__ == '__main__':
    all_teams = []
    #go get all the teams id numbers
    league = Team.load_team_info (NHL_season)
    
    #build a team class for each team 
    for t in league:
        team = Team (t, NHL_season)
        all_teams.append (team.team_pd)
        
    # put all the teams in a large data_frame
    list_of_teams = pd.concat (all_teams)
    
    #create the HTML
    html = list_of_teams.to_html(classes='table table-stripped')    
    text_file = open("index.html", "w")
    text_file.write(html)
    text_file.close()
