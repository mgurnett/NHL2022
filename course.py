#!/usr/bin/env python3

from michael_debug import debug_var
from json_write import *
from Read_API import *

if __name__ == '__main__':
    NHL_season = '20212022'
    
    url = (f'teams?season={NHL_season}')
    teams = read_API (url)
    
    for team in teams ['teams']:
        id = team ['id']
        name = team ['name']
        print (f'#{id} - {name}')