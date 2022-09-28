#!/usr/bin/env python3

# cd ~/Documents/GitHub/NHL2022 && source NHL2022_venv/bin/activate
# https://gitlab.com/dword4/nhlapi/-/blob/master/stats-api.md#teams
# https://nhl-api-explorer.herokuapp.com/

import json
import requests

Game_status_codes = [
    {"code": "1", "abstractGameState": "Preview", "detailedState": "Scheduled", "startTimeTBD": False},
    {"code": "2", "abstractGameState": "Preview", "detailedState": "Pre-Game", "startTimeTBD": False},
    {"code": "3", "abstractGameState": "Live", "detailedState": "In Progress",  "startTimeTBD": False},
    {"code": "4", "abstractGameState": "Live", "detailedState": "In Progress - Critical", "startTimeTBD": False},
    {"code": "5", "abstractGameState": "Final", "detailedState": "Game Over", "startTimeTBD": False},
    {"code": "6", "abstractGameState": "Final", "detailedState": "Final", "startTimeTBD": False},
    {"code": "7", "abstractGameState": "Final", "detailedState": "Final", "startTimeTBD": False},
    {"code": "8", "abstractGameState": "Preview", "detailedState": "Scheduled (Time TBD)", "startTimeTBD": False},
    {"code": "9", "abstractGameState": "Preview", "detailedState": "Postponed", "startTimeTBD": False} ]

Game_type = [
    {"id": "PR", "description": "Pre-season", "postseason": False},
    {"id": "R", "description": "Regular season", "postseason": False},
    {"id": "P", "description": "Playoffs", "postseason": True},
    {"id": "A", "description": "All-Star game", "postseason": False}  ]

# Set up the API call variables
base_URL = "https://statsapi.web.nhl.com/api/v1/"

def read_API(section, print_url = False):
    data = []
    url = base_URL + section
    if print_url == True:
        print (url)
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