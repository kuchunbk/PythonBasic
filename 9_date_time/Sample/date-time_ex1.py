'''Question: 
Write a Python script to display the various Date Time formats.
'''

# Python code: 

import time
import datetime
print("Current date and time: " , datetime.datetime.now())
print("Current year: ", datetime.date.today().strftime("%Y"))
print("Month of year: ", datetime.date.today().strftime("%B"))
print("Week number of the year: ", datetime.date.today().strftime("%W"))
print("Weekday of the week: ", datetime.date.today().strftime("%w"))
print("Day of year: ", datetime.date.today().strftime("%j"))
print("Day of the month : ", datetime.date.today().strftime("%d"))
print("Day of week: ", datetime.date.today().strftime("%A"))


'''Output sample: 
Current date and time:  2017-05-05 17:21:19.106836                                                            
Current year:  2017                                                                                           
Month of year:  May                                                                                           
Week number of the year:  18                                                                                  
Weekday of the week:  5                                                                                       
Day of year:  125                                                                                             
Day of the month :  05                                                                                        
Day of week:  Friday    
'''