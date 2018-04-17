'''Question: 
Write a Python program to print yesterday, today, tomorrow.
'''

# Python code: 

import datetime 
today = datetime.date.today()
yesterday = today - datetime.timedelta(days = 1)
tomorrow = today + datetime.timedelta(days = 1) 
print('Yesterday : ',yesterday)
print('Today : ',today)
print('Tomorrow : ',tomorrow)


'''Output sample: 
Yesterday :  2017-05-05                                                                                       
Today :  2017-05-06                                                                                           
Tomorrow :  2017-05-07  
'''