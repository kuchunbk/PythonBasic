'''Question: 
 Write a Python program to get OS name, platform and release information.
'''

# Python code: 

import platform
import os
print(os.name)
print(platform.system())
print(platform.release())


'''Output sample: 
posix                                                                                                         
Linux                                                                                                         
4.4.0-47-generic 
'''