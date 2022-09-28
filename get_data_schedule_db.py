#!/usr/bin/env python3

# https://statsapi.web.nhl.com/api/v1/schedule?season=20222023

# from michael_debug import debug_var
from Read_API import *
import pandas as pd

# NHL_season = '20212022'
NHL_season = '20222023'
 
def get_data (season):
    all_games = []
    # get the whole schedule
    schedule_dict = read_API (f'schedule?season={season}&date=2022-09-27', print_url=True)  #type dict
    games_list = schedule_dict ['dates'][0]['games']
    for g in games_list:
        games_debug = g #['gamePk'] # get the dataframe for it
        games_df = pd.json_normalize(g) # get the dataframe for it
        all_games.append (games_df)
    list_of_games = pd.concat (all_games)
    # print ("This is list_of_games" , list_of_games)
    return list_of_games

def write_out_html (html_file, name):
    text_file = open(f"{name}.html", "w")
    text_file.write(html_file)
    text_file.close() 

if __name__ == '__main__':
    sched_df = get_data(NHL_season)
    
#     print ("This is sched_df" , sched_df)
    schedule_html = sched_df.to_html(classes='table table-stripped') # convert the df to html
    # print ("This is schedule_html" , schedule_html)
    write_out_html (schedule_html, 'todays_games_new')