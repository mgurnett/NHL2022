#!/usr/bin/env python3

from michael_debug import debug_var
from json_write import *
from Read_API import *

if __name__ == '__main__':
    NHL_season = '20212022'
    
    url = (f'teams?season={NHL_season}')
    packages_json = read_API (url)
    for index in range (len(packages_json['teams'])):
        packages_str_id = json.dumps (packages_json['teams'][index]['id'])
        
        packages_str_name = json.dumps (packages_json['teams'][index]['name'])
        print (f'#{packages_str_id} - {packages_str_name}')