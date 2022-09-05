#!/usr/bin/env python3

from michael_debug import *
from data_classes import *
from json_write import *

if __name__ == '__main__':
    current_team = Team (22)
    print (current_team)
    
    json_team = json.dumps(current_team.__dict__)
    print (json_team)
    debug_var ("json_team", json_team)
    
    write_json (json_team, "NHL_teams")