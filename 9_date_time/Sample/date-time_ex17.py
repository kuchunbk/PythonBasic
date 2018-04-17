'''Question: 
Write a Python program to drop microseconds from datetime.
'''

# Python code: 

import datetime
dt = datetime.datetime.today().replace(microsecond=0)
print()
print(dt)
print()


'''Output sample: 
2017-05-06 14:17:47
'''