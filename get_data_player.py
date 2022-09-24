#!/usr/bin/env python3

# from michael_debug import debug_var
from Read_API import *
import pandas as pd

NHL_season = '20212022'
# NHL_season = '20222023'

class Player ():
    def __init__ (self, id, season):
        self.id = id
        self.season = season
        self.bio_url = (f'people/{str(self.id)}')
        self.stats_url = (f'people/{self.id}/stats?stats=statsSingleSeason&season={season}')
        self.get_data ()

    def __str__ (self):
        player_info = (f'{self.id}')
        return player_info
    
    def get_data (self):
        data = read_API (self.bio_url)  # get all the bio data for a single player
        player_bio_df = pd.json_normalize(data, record_path =['people']) # get the dataframe for it
        data = read_API (self.stats_url)  # get all the stats data for a single player
        subdata = data['stats'][0]['splits'][0]['stat']
        player_stats_df = pd.json_normalize(subdata) # get the dataframe for it
        print (player_stats_df)

        self.player_df = pd.concat ([player_bio_df, player_stats_df], axis=1, join="inner") # put the bio and stats together

        self.player_html = self.player_df.to_html(classes='table table-stripped') # convert the df to html

    @staticmethod  
    def load_people_info (team_id, season):
        roster_ids = []
        roster_of_players = []
        url_roster = (f'teams/{team_id}?expand=team.roster&season={season}')
        roster_str = read_API (url_roster)
        for pl in roster_str ['teams'][0]['roster']['roster']:
            roster_ids.append (pl ['person']['id'])
        print (roster_ids)
        for play in roster_ids:
            print (play)
            try:
                player = Player (play, season)
            except:
                print (f'{player} has no stats')
            else:
                roster_of_players.append (player.player_df)
                     
        list_of_teams = pd.concat (roster_of_players)
        html = list_of_teams.to_html(classes='table table-stripped')
        return (html) #html string
        
    @staticmethod  
    def update_stats (team_id, season):
        roster = []
        url_roster = (f'teams/{team_id}?expand=team.roster&season={season}')
        roster_str = read_API (url_roster)
        for p in roster_str ['teams'][0]['roster']['roster']:
            url_player = (f'people/{player_id}/stats?stats=statsSingleSeason&season={season}')        
            player_stats = read_API (url_local)
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

    # 8478402 Connor McDavid
    
    player = Player (8479973, NHL_season)
    player_html = player.player_html
    write_out_html (player_html)

    roster_html = Player.load_people_info (22, NHL_season)
    write_out_html (roster_html)
