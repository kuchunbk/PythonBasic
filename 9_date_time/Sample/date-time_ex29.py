'''Question: 
Write a Python program to get the GMT and local current time.
'''

# Python code: 

from time import gmtime, strftime
import time
print("\nGMT: "+time.strftime("%a, %d %b %Y %I:%M:%S %p %Z", time.gmtime()))
print("Local: "+strftime("%a, %d %b %Y %I:%M:%S %p %Z\n"))


'''Output sample: 
GMT: Mon, 08 May 2017 06:21:07 AM GMT                                                                         
Local: Mon, 08 May 2017 11:51:07 AM IST   
'''