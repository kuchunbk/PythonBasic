'''Question: 
Write a program to add year(s) with a given date and display the new date.
'''

# Python code: 

import datetime
from datetime import date
def addYears(d, years):
    try:
#Return same day of the current year        
        return d.replace(year = d.year + years)
    except ValueError:
#If not same day, it will return other, i.e.  February 29 to March 1 etc.        
        return d + (date(d.year + years, 1, 1) - date(d.year, 1, 1))

print(addYears(datetime.date(2015,1,1), -1))
print(addYears(datetime.date(2015,1,1), 0))
print(addYears(datetime.date(2015,1,1), 2))
print(addYears(datetime.date(2000,2,29),1))


'''Output sample: 
2014-01-01                                                                                                    
2015-01-01                                                                                                    
2017-01-01                                                                                                    
2001-03-01
'''