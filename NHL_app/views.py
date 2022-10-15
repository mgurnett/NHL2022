import pandas as pd
from flask import Flask, render_template
from datetime import datetime
# from PlayerClassSplit import *
# from LeagueClass import *
from get_data_schedule import *
from . import app

# https://code.visualstudio.com/docs/python/tutorial-flask#_create-and-run-a-minimal-flask-app

# NHL_season = '20212022'
NHL_season = '20222023'

def write_out_html (html_file, name):
    text_file = open(f"{name}.html", "w")
    text_file.write(html_file)
    text_file.close()

@app.route ('/schedule-date/<date_str>')
@app.route ('/schedule-date')
@app.route ('/')
def schedule_date(date_str = None): 
    titles = ['Game ID', 'Date', 'Away', 'Away score', 'Home', 'Home score', 'Venue']
    if date_str == None:
        today = date.today()
        d = today.strftime("%Y-%m-%d")
    else: 
        d = date_str
    sched_df = get_data(date = d, print_url = False)
    # print (sched_df.head)
    lesser_sched_df = sched_df [['gamePk', 
                                'gameDate', 
                                'status.abstractGameState', 
                                'teams.away.team.name', 
                                'teams.away.score', 
                                'teams.home.team.name', 
                                'teams.home.score', 
                                'venue.name']]
    # print (lesser_sched_df.head)
    # schedule_html = lesser_sched_df.describe().to_html() # convert the df to html

    # write_out_html (schedule_html, str(f'Games for {d}'))
    # return render_template("todays_games.html", games = schedule_html, titles = titles)
    return render_template('todays_games.html', games = lesser_sched_df.to_html(), titles = titles)

@app.route ('/schedule-team/<team_id>')
def schedule_team(team_id):  
    titles = ['Game ID', 'Date', 'Away', 'Away score', 'Home', 'Home score', 'Venue']
    sched_df = get_data(season = NHL_season, teamId = team_id, print_url=False)

    lesser_sched_df = sched_df [['gamePk', 
                                'gameDate', 
                                'status.abstractGameState', 
                                'teams.away.team.name', 
                                'teams.away.score', 
                                'teams.home.team.name', 
                                'teams.home.score', 
                                'venue.name']]
    # schedule_html = lesser_sched_df.to_html(classes='mystyle') # convert the df to html
    return render_template('todays_games.html', games = lesser_sched_df.to_html(classes='mystyle'), titles = titles)

@app.route ('/teams')
def teams():
    league = load_team_info (NHL_season) # league is a <class 'list'> of <class 'Team'>
    league = update_team_stats (league, NHL_season) # league is a <class 'list'> of <class 'Team'>
    teams = [team.to_dict() for team in league] # build a list of dicts from your objects
    json_string = json.dumps ({'teams': teams}, indent=2)  # serialize the whole thing
    
    return json_string