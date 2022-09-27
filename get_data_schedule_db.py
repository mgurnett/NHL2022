#!/usr/bin/env python3

# https://statsapi.web.nhl.com/api/v1/schedule?season=20222023

# from michael_debug import debug_var
from Read_API import *
import pandas as pd

# NHL_season = '20212022'
NHL_season = '20222023'
 
def get_data (season):
    schedule_str = read_API (f'schedule?season={season}&date=2022-09-25')
#     print (schedule_str)
    # get the whole schedule
    number_of_games = schedule_str ['totalGames']
    print (f'Number of games {number_of_games}')
    # XXX_dates = schedule_str ['dates']
    # print (XXX_dates)
    # XXX_games = XXX_dates ['totalGames']
    # print (XXX_games)

    # for g in schedule_str:
    #     # games_df = pd.json_normalize(data, record_path =['dates']['games']) # get the dataframe for it
    #     games_debug = str(g ['dates']['games'][0]) # get the dataframe for it
    #     print (games_debug)
    # return games_df

# def write_out_html (html_file, name):
#     text_file = open(f"{name}.html", "w")
#     text_file.write(html_file)
#     text_file.close() 

if __name__ == '__main__':
    sched_df = get_data(NHL_season)
    # schedule_html = sched_df.to_html(classes='table table-stripped') # convert the df to html
    # write_out_html (schedule_html, 'todays_games')