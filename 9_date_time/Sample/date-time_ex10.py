'''Question: 
Write a Python program to add 5 seconds with the current time.
'''

# Python code: 


import datetime
x= datetime.datetime.now()
y = x + datetime.timedelta(0,5)
print(x.time())
print(y.time())


'''Output sample: 
12:37:43.350241                                                                                               
12:37:48.350241 
'''