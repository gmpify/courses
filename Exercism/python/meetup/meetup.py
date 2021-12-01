import calendar
from datetime import date

def meetup(year, month, week, day_of_week):
    _, days = calendar.monthrange(year, month)
    possible_days = [day for day in range(1, days + 1) if date(year, month, day).strftime("%A") == day_of_week]

    if week == "teenth":
        for day in possible_days:
            if day in range(13,20):
                chosen_day = day
                break
    elif week == "1st":
        chosen_day = possible_days[0]
    elif week == "2nd":
        chosen_day = possible_days[1]
    elif week == "3rd":
        chosen_day = possible_days[2]
    elif week == "4th":
        chosen_day = possible_days[3]
    elif week == "5th":
        if len(possible_days) < 5:
            raise MeetupDayException("...")
        chosen_day = possible_days[4]
    elif week == "last":
        chosen_day = possible_days[-1]

    return date(year, month, chosen_day)

class MeetupDayException(Exception):
    pass
