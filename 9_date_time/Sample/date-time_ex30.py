'''Question: 
Write a Python program convert a date to timestamp.
'''

# Python code: 

import time
import datetime
now = datetime.datetime.now()
print()
print(time.mktime(now.timetuple()))
print()


'''Output sample: 
1494224813.0
'''