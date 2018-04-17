'''Question: 
 Write a Python program to subtract five days from current date.
'''

# Python code: 

from datetime import date, timedelta
dt = date.today() - timedelta(5)
print('Current Date :',date.today())
print('5 days before Current Date :',dt)


'''Output sample: 
Current Date : 2017-05-05                                                                                     
5 days before Current Date : 2017-04-30   
'''