'''Question: 
Write a Python program to find the location of Python module sources.
'''

# Python code: 

import sys
print("\nList of directories in sys module:")
print(sys.path)
print("\nList of directories in os module:")
import os
print(os.path)


'''Output sample: 
List of directories in sys module:                                      
['/home/students', '/usr/lib/python35.zip', '/usr/lib/python3.5', '/usr/
lib/python3.5/plat-x86_64-linux-gnu', '/usr/lib/python3.5/lib-dynload', 
'/usr/local/lib/python3.5/dist-packages', '/usr/lib/python3/dist-package
s']                                                                     
                                                                        
List of directories in os module:                                       
<module 'posixpath' from '/usr/lib/python3.5/posixpath.py'>
'''