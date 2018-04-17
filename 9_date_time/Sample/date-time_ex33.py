'''Question: 
Write a Python program to calculate number of days between two datetimes.
'''

# Python code: 

import datetime
from datetime import datetime

def differ_days(date1, date2):
    a = date1
    b = date2
    return (a-b).days
print()
print(differ_days((datetime(2016,10,12,0,0,0)), datetime(2015,12,10,0,0,0)))
print(differ_days((datetime(2016,10,12,0,0,0)), datetime(2015,12,10,23,59,59)))
print()


'''Output sample: 
307                                                                                                           
306
'''