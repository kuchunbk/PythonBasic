'''Question: 
 Write a Python program to get file creation and modification date/times.
'''

# Python code: 

import os.path, time
print("Last modified: %s" % time.ctime(os.path.getmtime("test.txt")))
print("Created: %s" % time.ctime(os.path.getctime("test.txt")))


'''Output sample: 
Last modified: Wed Apr 19 11:36:23 2017                                                                       
Created: Wed Apr 19 11:36:23 2017 
Python Code Editor:'''