'''Question: 
Write a Python program to get the date of the last Tuesday.
'''

# Python code: 

from datetime import date
from datetime import timedelta
today = date.today()
offset = (today.weekday() - 1) % 7
last_tuesday = today - timedelta(days=offset)
print(last_tuesday)


'''Output sample: 
2017-05-02 
'''