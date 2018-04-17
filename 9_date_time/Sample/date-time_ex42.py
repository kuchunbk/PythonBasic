'''Question: 
Write a Python program to display formatted text output of a month and start weeks on Sunday.
'''

# Python code: 

import calendar
cal = calendar.TextCalendar(calendar.SUNDAY)
print('First Month - 2022')
print(cal.prmonth(2022, 1))


'''Output sample: 
First Month - 2022                                                                                            
    January 2022                                                                                              
Su Mo Tu We Th Fr Sa                                                                                          
                   1                                                                                          
 2  3  4  5  6  7  8                                                                                          
 9 10 11 12 13 14 15                                                                                          
16 17 18 19 20 21 22                                                                                          
23 24 25 26 27 28 29                                                                                          
30 31                                                                                                         
 None 
'''