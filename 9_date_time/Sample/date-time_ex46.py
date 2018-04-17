'''Question: 
Write a Python program to create a HTML calendar with data for a specific year and month.
'''

# Python code: 

import calendar
htmlcal = calendar.HTMLCalendar(calendar.MONDAY)
print(htmlcal.formatmonth(2020, 12))


'''Output sample: 
                                              
December 2020                                                     
MonTueWedThuFriSatSun                                           
 123456                                                  
789101
11213                                                     
14151617181920                                                  
21222324252627                                                  
28293031                                   
           
'''