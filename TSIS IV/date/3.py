import datetime

# get the current datetime
now = datetime.datetime.now()

# drop microseconds from the datetime
now_without_microseconds = now.replace(microsecond=0)

# print the results
print("Current datetime (with microseconds):", now)
print("Current datetime (without microseconds):", now_without_microseconds)