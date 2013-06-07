"""
You are given the following information, but you may prefer to do some research for yourself.

    1 Jan 1900 was a Monday.
    Thirty days has September,
    April, June and November.
    All the rest have thirty-one,
    Saving February alone,
    Which has twenty-eight, rain or shine.
    And on leap years, twenty-nine.
    A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.

How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
"""
def month_days(month, leapyear):
    if month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12:
        return 31
    elif month==2:
        if leapyear:
            return 29
        else:
            return 28
    else:
        return 30
    
def leap_year(year):
    if year%4==0:
        if year%100==0:
            if year%400==0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

#initial var vals
#Jan 01 1900 == Monday
day = 1
month = 1
days_in_month = 31
year = 1900
day_of_week = 2
sundays = 0


while year !=2001:
    if year >1900:
        if day==1 and day_of_week==1:
            print "Sunday on", month, '/', day, '/', year
            sundays += 1
    day += 1
    day_of_week += 1
    if day_of_week >7:
        day_of_week =1
    if day > days_in_month:
        day = 1
        month += 1
    if month>12:
        month = 1
        year += 1
    days_in_month = month_days(month, leap_year(year))
print sundays
