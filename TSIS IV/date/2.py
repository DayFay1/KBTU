import datetime

# get today's date
today = datetime.date.today()

# get yesterday's date
yesterday = today - datetime.timedelta(days=1)

# get tomorrow's date
tomorrow = today + datetime.timedelta(days=1)

# print the dates
print("Yesterday was:", yesterday)
print("Today is:", today)
print("Tomorrow will be:", tomorrow)