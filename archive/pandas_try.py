#!/usr/bin/env python3

from Read_API import *
import pandas as pd
import json

NHL_season = '20212022'
sub_url = f'teams/{22}?expand=team.roster&season={NHL_season}'

data = read_API (sub_url)

df_nested_list = pd.json_normalize(data, record_path =['teams'])
df_team_info = df_nested_list.drop('roster.roster', axis=1)

html = df_team_info.to_html(classes='table table-stripped')
# write html to file
text_file = open("index.html", "w")
text_file.write(html)
text_file.close()