'''Question: 
Write a python program to generate a date and time as a string.
'''

# Python code: 

import datetime
# Current time
now = datetime.datetime.now()
# Make a note of the date and time in a string
# Date and time in string : 2016-11-05 11:24:24 PM
datestr = "# In string: " + now.strftime("%Y-%m-%d %H:%M:%S %p") + "\n"
print()
print(datestr)
print()


'''Output sample: 
# In string: 2017-05-08 14:24:37 PM
'''