'''Question: 
Write a Python program convert a string date to the timestamp.
'''

# Python code: 

import time
import datetime
s = "01/10/2016"
print()
print(time.mktime(datetime.datetime.strptime(s, "%d/%m/%Y").timetuple()))
print()


'''Output sample: 
1494225605.0  
'''