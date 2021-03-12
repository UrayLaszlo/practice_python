import calendar

def date_time(time):
    day = str(int(time[0:2]))
    pos_mon = int(time[time.find('.')+1:time.find(".", 4, 6)])
    mon = calendar.month_name[pos_mon]
    year = time[time.find(".", 3, 9)+1:-6]
    hours = str(int(time[time.find(' ', 8):-3]))
    minutes = str(int(time[-2:]))
    hour_str = ''
    min_str = ''
    if int(hours) == 1:
        hour_str = 'hour'
    else:
        hour_str = 'hours'
    if int(minutes) == 1:
        min_str = 'minute'
    else: 
        min_str = 'minutes'
    #return str(int(time[0:2])) + ' ' + calendar.month_name[int(time[time.find('.')+1:time.find(".", 4, 6)])] + ' ' + time[time.find(".", 3, 9)+1:-6] + " year " + str(int(time[time.find(' ', 8):-3])) + " hours " + str(int(time[-2:])) + " minutes"
    return day + ' ' + mon + ' ' + year + ' year ' + hours + ' ' + hour_str + ' ' + minutes + ' ' + min_str

date_time("01.01.2000 01:00") # "1 January 2000 year 0 hours 0 minutes", "Millenium"
date_time("09.05.1945 06:30") # "9 May 1945 year 6 hours 30 minutes", "Victory"
date_time("20.11.1990 03:55") # "20 November 1990 year 3 hours 55 minutes", "Somebody was born"
