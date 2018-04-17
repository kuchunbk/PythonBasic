'''Question: 
Write a Python program to get the current date time information.
'''

# Python code: 

import time
import datetime

print()
print("Time in seconds since the epoch: %s" %time.time())
print("Current date and time: " , datetime.datetime.now())
print("Alternate date and time: " ,datetime.datetime.now().strftime("%y-%m-%d-%H-%M"))
print("Current year: ", datetime.date.today().strftime("%Y"))
print("Month of year: ", datetime.date.today().strftime("%B"))
print("Week number of the year: ", datetime.date.today().strftime("%W"))
print("Weekday of the week: ", datetime.date.today().strftime("%w"))
print("Day of year: ", datetime.date.today().strftime("%j"))
print("Day of the month : ", datetime.date.today().strftime("%d"))
print("Day of week: ", datetime.date.today().strftime("%A"))
print()


'''Output sample: 
Time in seconds since the epoch: 1494232844.031525                                                            
Current date and time:  2017-05-08 14:10:44.031541                                                            
Alternate date and time:  17-05-08-14-10                                                                      
Current year:  2017                                                                                           
Month of year:  May                                                                                           
Week number of the year:  19                                                                                  
Weekday of the week:  1                                                                                       
Day of year:  128                                                                                             
Day of the month :  08                                                                                        
Day of week:  Monday 
'''