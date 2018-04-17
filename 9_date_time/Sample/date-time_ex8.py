'''Question: 
Write a Python program to convert the date to datetime (midnight of the date).
'''

# Python code: 

">
from datetime import date
from datetime import datetime
dt = date.today()
print(datetime.combine(dt, datetime.min.time()))


'''Output sample: 
2017-05-06 00:00:00  
'''