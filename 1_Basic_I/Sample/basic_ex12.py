'''Question: 
Write a Python program to print the calendar of a given month and year.
'''

# Python code: 

import calendar
y = int(input("Input the year : "))
m = int(input("Input the month : "))
print(calendar.month(y, m))

'''Output sample: 
Input the year : 2017                                                                                         
Input the month : 04                                                                                          
     April 2017                                                                                               
Mo Tu We Th Fr Sa Su                                                                                          
                1  2                                                                                          
 3  4  5  6  7  8  9                                                                                          
10 11 12 13 14 15 16                                                                                          
17 18 19 20 21 22 23                                                                                          
24 25 26 27 28 29 30 
'''