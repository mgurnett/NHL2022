#!/usr/bin/env python3
# NHL_season = '20212022'
NHL_season = '20222023'
 
def get_data (season = "", date = "", team = 0):
    modifiers = 0
    all_games = []
    # get the whole schedule
    if season != "":
        season_url = (f'season={season}')
        modifiers +=1
    else:
        season_url = ''
    if team != 0:
        team_url = (f'team={team}')
        modifiers +=1
    else:
        team_url = ''
    if date != "":
        date_url = (f'date={date}')
        modifiers +=1

    if modifiers > 0:
        quest_url = "?"
    else:
        quest_url = ""

    if modifiers > 1:
        comma_url = ","
    else:
        comma_url = ""

    schedule_url = (f'schedule{quest_url}{season_url}{comma_url}{team_url}{comma_url}{date_url}')
    print (schedule_url)
   
if __name__ == '__main__':
    sched_df = get_data(season = NHL_season, date = "2002-09-28", team = 20)

    sched_df = get_data(date = "2002-09-28", team = 20)
