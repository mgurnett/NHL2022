#!/usr/bin/env python3

import json
import requests
import pandas as pd
from Read_API import *
from PlayerClass import *
from TeamClass import *

def get_league ():
    team_list = [] # this is a list
#     url = 'teams'
    url = 'teams?season=20222023'
    packages_json = read_API (url)
    for index in range (len(packages_json['teams'])):
        team_id = packages_json['teams'][index]['id']
        current_team = Team (team_id)
        current_team.name = packages_json['teams'][index]['name']
        current_team.abbreviation = packages_json['teams'][index]['abbreviation']
        current_team.teamName = packages_json['teams'][index]['teamName']
        current_team.locationName = packages_json['teams'][index]['locationName']
        current_team.shortName = packages_json['teams'][index]['shortName']
        current_team.division = packages_json['teams'][index]['division']['name']
        current_team.venue = packages_json['teams'][index]['venue']['name']
        current_team.roster = Team.get_roster (team_id)
        team_list.append (current_team)
        print (current_team)
    return (team_list)        
        
if __name__ == '__main__':
    league = get_league ()
