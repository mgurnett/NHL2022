#!/usr/bin/env python3

from Read_API import *
import pandas as pd
import json

NHL_season = '20212022'
sub_url = f'teams/{22}?expand=team.roster&season={NHL_season}'

data = read_API (sub_url)

df_nested_list = pd.json_normalize(data, record_path =['teams'])

print (df_nested_list.to_string())
html = df_nested_list.to_html()
print(html)