import datetime

# get input dates from user
date_str1 = input("Enter the first date in YYYY-MM-DD HH:MM:SS format: ")
date_str2 = input("Enter the second date in YYYY-MM-DD HH:MM:SS format: ")

# convert input strings to datetime objects
date1 = datetime.datetime.strptime(date_str1, '%Y-%m-%d %H:%M:%S')
date2 = datetime.datetime.strptime(date_str2, '%Y-%m-%d %H:%M:%S')

# calculate the difference in seconds
diff_seconds = (date2 - date1).total_seconds()

# display the result
print("The difference between the two dates is {} seconds.".format(diff_seconds))