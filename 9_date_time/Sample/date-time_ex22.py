'''Question: 
Write a Python program to get the number of days of a given month and year.
'''

# Python code: 

from calendar import monthrange
year = 2016
month = 2
print(monthrange(year, month))


'''Output sample: 
(0, 29)
'''