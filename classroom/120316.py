__author__ = 'anastasiiakorosteleva'

#!/usr/bin/python3.3.0


import pyowm #  OpenWeatherMap API wrapper
from time import ctime #  function makes string with time from seconds
import argparse #  best practice to define arguments

# creating parser object with description of what our script does
parser = argparse.ArgumentParser(description="Shows current weather "
                                             "and forecasts in "
                                             "selected city")
# adding argument 'city' with type str and default value Saint-Petersburg
parser.add_argument("city",
                    type=str,
                    default="Saint-Petersbug",
                    nargs="?",
                    help="Selected   city to show weather in")
# adding argument optional '--day' with type int and choices [0, 1, 2, 3, 4]
parser.add_argument('--day',
                    type=int,
                    default=0,
                    choices=[0, 1, 2, 3, 4],
                    help="day to show weather: 0 for today,"
                         " 1 for tomorrow and so on. "
                         "default value is 0")

# HERE WE PARSE ARGUMENTS FROM sys.argv
args = parser.parse_args()  # eats sys.argv
city = args.city  # arguments city is available as attribute
day = args.day    # arguments day  is available as attribute

# function return string representation of Weather object from pyowm library
def format_weather(w):
    data = [
        ctime(w.get_reference_time()),  # time
        w.get_status(),  # status
        str(w.get_temperature(unit="celsius")["temp"])  # temperature
    ]
    return " ".join(data)

# here provide your api key
owm = pyowm.OWM("")

# getting current weather
observation = owm.weather_at_place(city)
w = observation.get_weather()

# creating list with current weather
time_points = [format_weather(w)]

# getting forecasts for next 5 days
fc = owm.three_hours_forecast(city)
f = fc.get_forecast()
# adding forecasts to out list
for weather in f:
    time_points.append(format_weather(weather))

# getting curent date
date_start = time_points[0][4:10]
print(date_start)

# check when date changes
for i, time_point in enumerate(time_points):
    if date_start not in time_point:
        break

if day == 0:
    for time_point in time_points[0:i]:
        print(time_point)
else:
    for time_point in time_points[i + (day - 1) * 8:i + day * 8]:
        print(time_point)