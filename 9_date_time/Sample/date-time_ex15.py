'''Question: 
Write a Python program to select all the Sundays of a specified year.
'''

# Python code: 

from datetime import date, timedelta

def all_sundays(year):
# January 1st of the given year
       dt = date(year, 1, 1)
# First Sunday of the given year       
       dt += timedelta(days = 6 - dt.weekday())  
       while dt.year == year:
          yield dt
          dt += timedelta(days = 7)
          
for s in all_sundays(2020):
   print(s)
   

'''Output sample: 
2020-01-05                                                                                                    
2020-01-12                                                                                                    
2020-01-19                                                                                                    
2020-01-26                                                                                                    
2020-02-02     
-----
2020-12-06                                                                                                    
2020-12-13                                                                                                    
2020-12-20                                                                                                    
2020-12-27   
'''