'''Question: 
Write a Python program to retrieve file properties.
'''

# Python code: 

import os.path
import time

print('File         :', __file__)
print('Access time  :', time.ctime(os.path.getatime(__file__)))
print('Modified time:', time.ctime(os.path.getmtime(__file__)))
print('Change time  :', time.ctime(os.path.getctime(__file__)))
print('Size         :', os.path.getsize(__file__))


'''Output sample: 
File         : 8dbacd90-266d-11e7-a9c1-cf681af3cdf1.py             
Access time  : Fri Apr 21 14:06:03 2017                            
Modified time: Fri Apr 21 14:06:02 2017                            
Change time  : Fri Apr 21 14:06:02 2017                            
Size         : 304   
'''