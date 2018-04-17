'''Question: 
Write a Python program to get the last day of a specified year and month.
'''

# Python code: 


import calendar
year = 2015
month = 2
print(calendar.monthrange(year, month)[1])


'''Output sample: 
28 
'''