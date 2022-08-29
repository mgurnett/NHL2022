#!/usr/bin/env python3

import json
import requests
import pandas as pd
from Read_API import *
from PlayerClass import *
from TeamClass import *

def get_league ():
    league = [] # this is a list
    packages_json = read_API ('teams')
    print (packages_json)
        


if __name__ == '__main__':
    get_league ()
