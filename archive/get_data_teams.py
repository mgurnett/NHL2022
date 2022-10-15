#!/usr/bin/env python3

# from michael_debug import debug_var
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
        url_local = (f'teams?season={season}')
        teams = read_API (url_local)
        for t in teams ['teams']:
            team_id = t ['id']
            team = Team (team_id, NHL_season)
            leag.append (team.team_pd)
        
        list_of_teams = pd.concat (leag)
        html = list_of_teams.to_html(classes='table table-stripped')
        
        return (html) #html string
    
def write_out_html (html_file):
    text_file = open("index.html", "w")
    text_file.write(html_file)
    text_file.close()

if __name__ == '__main__':
    league_html = Team.load_team_info (NHL_season)
