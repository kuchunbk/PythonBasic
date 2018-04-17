'''Question: 
Write a Python program to convert Year/Month/Day to Day of Year.
'''

# Python code: 

import datetime
today = datetime.datetime.now()
day_of_year = (today - datetime.datetime(today.year, 1, 1)).days + 1
print(day_of_year)


'''Output sample: 
126
'''