import pandas as pd
from flask import Flask, render_template
from datetime import datetime
from PlayerClassSplit import *
from LeagueClass import *
from get_data_schedule import *

# https://code.visualstudio.com/docs/python/tutorial-flask#_create-and-run-a-minimal-flask-app

NHL_season = '20212022'
# NHL_season = '20222023'
app = Flask (__name__)

# Replace the existing home function with the one below
@app.route("/")
def home():
    return render_template("home.html")

# New functions
@app.route("/about/")
def about():
    return render_template("about.html")

@app.route("/contact/")
def contact():
    return render_template("contact.html")


@app.route("/hello/")
@app.route("/hello/<name>")
def hello_there(name = None):
    return render_template(
        "hello_there.html",
        name=name,
        date=datetime.now()
    )

@app.route ('/players')
def players():
    screen = []
    league = load_team_info (NHL_season)
    current_team = Team (22, NHL_season)
    print (current_team.roster)
    for player in current_team.roster:
        try:
#             print_player = Player (player, NHL_season)
            print_player = get_a_new_player (player, NHL_season)
        except:
            print(f"{player} is not an active player")
        else:
            print(str(print_player))
            screen.append (str(print_player))
    return str(screen)

@app.route ('/player')
def player():
    player = get_a_new_player (8478402, NHL_season)
    return str(player)

@app.route ('/table')
def table():
    sub_url = f'teams/{22}?expand=team.roster&season={NHL_season}'

    data = read_API (sub_url)

    df_nested_list = pd.json_normalize(data, record_path =['teams'])

    df_team_info = df_nested_list.drop('roster.roster', axis=1)

    html = df_team_info.to_html(classes='table table-stripped')
    return html

@app.route ('/teams')
def teams():
    league = load_team_info (NHL_season) # league is a <class 'list'> of <class 'Team'>
    league = update_team_stats (league, NHL_season) # league is a <class 'list'> of <class 'Team'>
    teams = [team.to_dict() for team in league] # build a list of dicts from your objects
    json_string = json.dumps ({'teams': teams}, indent=2)  # serialize the whole thing
    
    return json_string

# @app.route ('/schedule')
# def schedule():
#     schedule_html = '''
#     <html>
#       <head><title>HTML Pandas Dataframe with CSS</title></head>
#       <link rel="stylesheet" type="text/css" href="/df_style.css"/>
#     '''
#     sched_df = get_data(season = NHL_season, teamId = 22, print_url=False)
#     schedule_html = sched_df.to_html(classes='mystyle') # convert the df to html
    
#     return schedule_html

@app.route ('/schedule/<teamId>')
def schedule(teamId):
    sched_df = get_data(season = NHL_season, teamId = teamId, print_url=False)
    schedule_html = sched_df.to_html(classes='mystyle') # convert the df to html
    return schedule_html

@app.route ('/schedule-date/<date_str>')
@app.route ('/schedule-date')
def schedule_date(date_str = None): 
    if date_str == None:
        today = date.today()
        d = today.strftime("%Y-%m-%d")
    else: 
        d = date_str
    sched_df = get_data(date = d)
    schedule_html = sched_df.to_html(classes='mystyle') # convert the df to html
    return schedule_html

# if __name__ == '__main__':
#     pass