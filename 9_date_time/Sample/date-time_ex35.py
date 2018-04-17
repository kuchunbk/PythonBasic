'''Question: 
Write a Python program to convert a date to Unix timestamp.
'''

# Python code: 

import datetime
import time
dt = datetime.datetime(2016, 2, 25, 23, 23)
print()
print("Unix Timestamp: ",(time.mktime(dt.timetuple())))
print()


'''Output sample: 
Unix Timestamp:  1456422780.0 
'''