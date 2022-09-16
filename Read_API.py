#!/usr/bin/env python3

# cd ~/Documents/GitHub/NHL2022 && source NHL2022_venv/bin/activate
# https://gitlab.com/dword4/nhlapi/-/blob/master/stats-api.md#teams

import json
import requests

# Set up the API call variables
base_URL = "https://statsapi.web.nhl.com/api/v1/"

def read_API(section):
    data = []
    url = base_URL + section
#     print (url)
    r = requests.get(url)
    if r.status_code != 200:
        return print(f"status code is {r.status_code} for {url}")
    else:
        data = r.json()
        return data
 

if __name__ == '__main__':
    # url = 'schedule?date=2021-03-27'
    url = 'teams/22/stats?season=20212022'
    packages_json = read_API (url)
    packages_str = json.dumps (packages_json['stats'][0]['splits'][0]['stat']['gamesPlayed'], indent =2)
#     packages_str = json.dumps (packages_json['teams'][0]['division']['name'], indent =2)
    print (packages_str)