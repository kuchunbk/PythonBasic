'''Question: 
Write a Python program to find the date of the first Monday of a given week.
'''

# Python code: 

import time
print(time.asctime(time.strptime('2015 50 1', '%Y %W %w')))


'''Output sample: 
Mon Dec 14 00:00:00 2015  
'''