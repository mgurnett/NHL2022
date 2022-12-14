#!/usr/bin/env python3

# https://statsapi.web.nhl.com/api/v1/schedule?season=20222023

from datetime import date

import pandas as pd

# from michael_debug import debug_var
from Read_API import *

# NHL_season = '20212022'
NHL_season = '20222023'

def get_data (print_url = False, **kwargs):
    modifiers = len (kwargs)
    
    if modifiers == 0:
        schedule_url = (f'schedule')
    else:
        mods_url = ""
        for key, value in kwargs.items():
            mods_url += str(f'{key}={value}&')
        schedule_url = (f'schedule?'+mods_url)
        if 'teamId' in kwargs:
            byteam = True
        else:
            byteam = False
    
    if print_url == True: #debug issue
        print (f'The output URL is: {schedule_url}')

    all_games = []

    schedule_dict = read_API (schedule_url, print_url=False)  #type dict
    if byteam:
        games_list = schedule_dict ['dates'] #by team]
    else:
        games_list = schedule_dict ['dates'][0]['games'] #by date
    # print (f'This is the games list {games_list}')

    for g in games_list:
        print (f'This is g - {g}')
        # games_debug = g ['gamePk'] # get the dataframe for it
        # games_debug = g ['games'][0]['gamePk'] # get the dataframe for it
        # print (f'games_debug is {games_debug}')
        if byteam:
            games_df = pd.json_normalize(g['games']) # get the dataframe for it
        else:
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
    # sched_df = get_data(season = NHL_season)
    # schedule_html += sched_df.to_html(classes='mystyle') # convert the df to html
    # # print ("This is schedule_html" , schedule_html)
    # write_out_html (schedule_html, 'todays_games_new1')

    date_str = "2022-10-05"
    # date_str = None
    if date_str == None:
        today = date.today()
        d = today.strftime("%Y-%m-%d")
    else: 
        d = date_str
    sched_df = get_data(date = d, print_url = False)
    lesser_sched_df = sched_df [['gamePk', 
                                'gameDate', 
                                'status.abstractGameState', 
                                'teams.away.team.name', 
                                'teams.away.score', 
                                'teams.home.team.name', 
                                'teams.home.score', 
                                'venue.name']]
    schedule_html = lesser_sched_df.to_html(classes='mystyle') # convert the df to html

    # print ("This is schedule_html" , schedule_html)
    write_out_html (schedule_html, str(f'Games for {d}'))

    sched_df = get_data(season = NHL_season, teamId = 22, print_url=False)
    schedule_html = sched_df.to_html(classes='mystyle') # convert the df to html
    # print ("This is schedule_html" , schedule_html)
    write_out_html (schedule_html, 'Oilers schedule')
