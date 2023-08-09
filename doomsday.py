from datetime import date
from datetime import timedelta
import random
"""
https://en.wikipedia.org/wiki/Doomsday_rule

1. Determination of the anchor day for the century
2. Calculation of the anchor day for the year from the one for the century
3. Selection of the closest date out of those that always fall on the doomsday, e.g., 4/4 and 6/6
4. Count of the number of days (modulo 7) between that date and the date in question to arrive at the day of the week

Anchor days for 3 centuries
    1700-1799   Noneday     America was None beginning of this century
    1800-1899   Friday      Industrial age - working, yearned for Fridays (???)
    1900-1999   Wednesday   We-in-dis-day (Most born this century)
    2000-2099   Tuesday     Y-Tue-K day
    2100-2199   Noneday     Start of new century

Day Mnemonics
    Sunday      0   Noneday
    Monday      1   Oneday
    Tuesday     2   Twosday
    Wednesday   3   Treblesday
    Thursday    4   Foursday
    Friday      5   Fiveday
    Saturday	6   Six-a-day

Memorable dates
    January     1/3 (1/4)   3 every 1-3, 4 every 4
    February    2/28 (2/29) last day
    March       3/14        pi day
    April       4/4
    May         5/9         9 to 5 at 7-11
    June        6/6
    July        7/11
    August      8/8
    September   9/11
    October     10/10
    November    11/7
    December    12/12

Other
    2/14
    7/4
    12/26

Finding a year's anchor day (Steps 1 & 2 from above)
1. Divide last two digits of the year (call this y) by 12, to get a: the floor of the quotient
2. Let b be the remainder of above quotient
3. Divide the remainder by 4, and let c be the floor of the quotient
4. Let d be the sum of the three numbers (a + b + c = d) 
5. Count forward the specified number of days (d, or d%7) from the anchor day to get the year's one
"""

# TODO: add argparse for changing range
start_date_range = date(1700, 1, 1)
end_date_range = date(2199, 12, 31)


def get_anchor_for_century(year):
    c = year // 100
    if c == 17:
        return 0
    if c == 18:
        return 5
    if c == 19:
        return 3
    if c == 20:
        return 2
    if c == 21:
        return 0
    
# get the parameters for the formula (for checking where we went wrong during a calculation) in str format
def get_parameters(year):
    century_anchor = get_anchor_for_century(year)
    # Divide last two digits of the year (call this y) by 12, to get a: the floor of the quotient
    y = year % 100
    a = y // 12
    # Let b be the remainder of above quotient
    b = y % 12
    # Divide the remainder by 4, and let c be the floor of the quotient
    c = b // 4
    # Let d be the sum of the three numbers (a + b + c = d) 
    d = a + b + c
    # Count forward the specified number of days (d, or d%7) from the anchor day to get the year's one
    return "a: {}\nb: {}\nc: {}\nd: {}\ncentury_anchor: {}\nyear_anchor: {}".format(a, b, c, d, century_anchor, (d+century_anchor) % 7)

def quiz():
    difference = end_date_range - start_date_range
    random_date = start_date_range + timedelta(random.randint(0, difference.days))
    day_of_week = random_date.strftime("%A")
    formatted_date = random_date.strftime("%B %d, %Y").replace(' 0', ' ')
    answer = input(formatted_date + "?\n").lower().strip()
    if answer == "q":
        exit()
    elif answer == day_of_week.lower():
        print("Correct!")
    else:
        print("Incorrect: " + day_of_week)

    # print values for the formula for troubleshooting incorrect answers
    # TODO: add argparse and flag
    print(get_parameters(random_date.year))
    if (random_date.year % 4 == 0):
        print("Leap year")
    print("")

if __name__ == '__main__':
    print("Enter the day of the week for the given date, enter 'q' to quit.")
    while True:
        quiz()