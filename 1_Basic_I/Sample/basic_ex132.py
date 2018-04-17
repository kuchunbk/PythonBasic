'''Question: 
Write a Python program to list home directory without absolute path.
'''

# Python code: 

import os.path
print(os.path.expanduser('~'))


'''Output sample: 
/home/students
'''