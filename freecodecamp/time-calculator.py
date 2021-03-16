def add_time(start, duration='0:00', day=""):
    output = ''
    days = ['monday', 'tuesday', 'wednesday',
            'thursday', 'friday', 'saturday', 'sunday']

    # list starting time
    hours = list(start.split(":"))
    minutes = list(hours[1].split(" "))
    hour = int(hours[0])  # Starting hour
    minute = int(minutes[0])  # Starting minute
    ampm = minutes[1]  # AM PM

    # list additional duration time
    duration_time = list(duration.split(":"))
    duration_hour = int(duration_time[0])
    duration_minute = int(duration_time[1])

    # get the total minutes from start and duration
    total_minutes = minute+duration_minute
    # count the hours for every 60 minutes
    additional_hour = total_minutes // 60
    # get exceded minutes from 60 minutes
    minutes_remainder = total_minutes % 60
    # add start and duration hour
    total_hours = hour + additional_hour + duration_hour

    # add 12 hours to total hours if its PM
    if (ampm == "PM"):
        total_hours += 12

    # check if total hour is above 24 and determine the number of days
    # count the day for every 24 hours
    additional_day = total_hours // 24
    # get exceded minutes from 60 minutes
    hour_remainder = total_hours % 24

    # check if hour is above 13 and reset to 1 for 12 hour format
    adjusted_hour = hour_remainder
    if(hour_remainder >= 13):
        adjusted_hour -= 12
    if(hour_remainder == 0):
        adjusted_hour = 12

    # print('hour remainder:', hour_remainder)
    # print('total hours:', total_hours)
    # print('additional day:', additional_day)
    # print hour:minutes
    output += f"{adjusted_hour}:"
    output += "{:02} ".format(minutes_remainder)

    # print AM PM  0 - 12 - AM 12 - 24 - PM
    # print('hour remainder: ', hour_remainder < 12)
    output += "AM" if (hour_remainder < 12) else "PM"

    # check if weekday is valid
    if bool(day) and day.upper() in map(str.upper, days):
        # find the key of the weekday using next
        key = next((key for key, val in enumerate(days)
                    if val.upper() == day.upper()), None)

        output += ", " + days[(key+additional_day) % 7].capitalize()

    # print next day or n days later
    if(additional_day == 1 and total_hours >= 13):
        output += " (next day)"
    elif(additional_day > 1):
        output += f" ({additional_day} days later)"

    return output


print(add_time("11:59 PM", "24:05"))
