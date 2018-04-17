'''Question: 
Write a Python program to test the third Tuesday of a month.
'''

# Python code: 

from datetime import datetime 
def is_third_tuesday(s):
    d = datetime.strptime(s, '%b %d, %Y')
    return d.weekday() == 1 and 14 < d.day < 22

print(is_third_tuesday('Jun 23, 2015')) #False
print(is_third_tuesday('Jun 16, 2015')) #True 
print(is_third_tuesday('Jul 21, 2015')) #False


'''Output sample: 
False                                                                
True                                                                 
True
'''