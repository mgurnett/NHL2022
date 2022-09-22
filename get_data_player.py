#!/usr/bin/env python3

# from michael_debug import debug_var
from Read_API import *
import pandas as pd

# NHL_season = '20212022'
NHL_season = '20222023'

class Player ():
    def __init__ (self, id, season):
        self.id = id
        self.season = season
        self.sub_url = (f'people/{str(self.id)}')
        self.get_data ()
    
    def get_data (self):
        data = read_API (self.sub_url)

        self.player_pd = pd.json_normalize(data, record_path =['people'])
        self.player_html = self.player_pd.to_html(classes='table table-stripped')
        
    @staticmethod  
    def load_people_info (team_id, season):
        roster = []
        url_local = (f'teams/{team_id}?expand=team.roster&season={season}')
        roster_str = read_API (url_local)
        for p in roster_str ['teams'][0]['roster']['roster']:
            current_player = p ['person']['id']
            player = Player (current_player, season)
            roster.append (player.player_pd)          
        
        list_of_teams = pd.concat (roster)
        html = list_of_teams.to_html(classes='table table-stripped')
        
        return (html) #html string
    
def write_out_html (html_file):
    text_file = open("index.html", "w")
    text_file.write(html_file)
    text_file.close()

if __name__ == '__main__':
#     8478402 Connor McDavid
#     player = Player (8478402, NHL_season)
#     player_html = player.player_html
#     write_out_html (player_html)

    roster_html = Player.load_people_info (22, NHL_season)
    write_out_html (roster_html)
