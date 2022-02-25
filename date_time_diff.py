""" Date & Time difference between two dates. """

from datetime import datetime

D1 = "2021-06-21"
D2 = "2021-02-19"
D3 = "2021-06-21 12:00:00"
D4 = "2021-02-19 21:30:00"
D5 = "May 21, 2021"
D6 = "Feb 28, 2022"

def date_convertor_d1_d2(date_str):
    """ date time convertor for D1 & D2 """
    return datetime.strptime(date_str, "%Y-%m-%d")

def date_convertor_d3_d4(date_str):
    """ date time convertor for D3 & D4 """
    return datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")

def date_convertor_d5_d6(date_str):
    """ date time convertor for D5 & D6 """
    return datetime.strptime(date_str, "%b %d, %Y")

def cal_date_time_diff(date_time1, date_time2):
    """ Calculate date & time difference between two dates. """
    diff = date_time1 - date_time2
    date_time_list = str(diff).split(",")
    date = date_time_list[0].split(",")
    time = date_time_list[1].split(":")
    seconds = time[2]
    minutes = time[1]
    hours = time[0]
    days = date[0]
    return seconds, minutes, hours, days

def display_date_diff(diff_dt):
    """ Display date time difference between two dates. """
    print(diff_dt[0] + " seconds",
          diff_dt[1] + " minutes",
          diff_dt[2] + " hours",
          diff_dt[3] + " & days")

d1 = date_convertor_d1_d2(D1)
d2 = date_convertor_d1_d2(D2)
date_diff = cal_date_time_diff(d1,d2)
print("\nDifference between " + D1 + " & " + D2)
display_date_diff(date_diff)

d3 = date_convertor_d3_d4(D3)
d4 = date_convertor_d3_d4(D4)
date_diff = cal_date_time_diff(d3,d4)
print("\nDifference between " + D3 + " & " + D4)
display_date_diff(date_diff)

d5 = date_convertor_d5_d6(D5)
d6 = date_convertor_d5_d6(D6)
date_diff = cal_date_time_diff(d5,d6)
print("\nDifference between " + D5 + " & " + D6)
display_date_diff(date_diff)
