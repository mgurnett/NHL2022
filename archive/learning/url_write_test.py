#!/usr/bin/env python3
# NHL_season = '20212022'
NHL_season = '20222023'
 
def get_data (**kwargs):
    modifiers = len (kwargs)
    
    if modifiers == 0:
        schedule_url = (f'schedule')
    else:
        mods_url = ""
        for key, value in kwargs.items():
            mods_url += str(f'{key}={value}&')
        schedule_url = (f'schedule?'+mods_url)

    print (f'The output URL is: {schedule_url}')
   
if __name__ == '__main__':
   
    sched_df = get_data()
    
    sched_df = get_data(season = NHL_season, date = "2022-09-28", teamId = 22)

    sched_df = get_data(date = "2022-09-29", teamId = 22)


