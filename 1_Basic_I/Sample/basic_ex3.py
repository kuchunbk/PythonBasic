'''Question: 
Write a Python program to display the current date and time.
'''

# Python code: 

import datetime
now = datetime.datetime.now()
print ("Current date and time : ")
print (now.strftime("%Y-%m-%d %H:%M:%S"))


'''Output sample: 
Current date and time : 
2014-07-05 14:34:14
'''