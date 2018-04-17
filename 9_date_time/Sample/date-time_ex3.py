'''Question: 
Write a Python program to convert a string to datetime.
'''

# Python code: 

from datetime import datetime
date_object = datetime.strptime('Jul 1 2014 2:43PM', '%b %d %Y %I:%M%p')
print(date_object)


'''Output sample: 
2014-07-01 14:43:00 
'''