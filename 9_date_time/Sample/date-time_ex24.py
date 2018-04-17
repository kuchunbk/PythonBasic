'''Question: 
Write a Python program to count the number of Monday of the 1st day of the month from 2015 to 2016.
'''

# Python code: 

import datetime
from datetime import datetime
monday1 = 0
months = range(1,13)
for year in range(2015, 2017):
    for month in months:
        if datetime(year, month, 1).weekday() == 0:
            monday1 += 1
print(monday1)


'''Output sample: 
3
'''