import datetime

# get the first date from the user
date1_str = input("Enter the first date (YYYY-MM-DD HH:MM:SS): ")
date1 = datetime.datetime.strptime(date1_str, '%Y-%m-%d %H:%M:%S')

# get the second date from the user
date2_str = input("Enter the second date (YYYY-MM-DD HH:MM:SS): ")
date2 = datetime.datetime.strptime(date2_str, '%Y-%m-%d %H:%M:%S')

# calculate the difference between the dates in seconds
difference_in_seconds = (date2 - date1).total_seconds()

# print the result
print("Difference between the two dates in seconds:", difference_in_seconds)