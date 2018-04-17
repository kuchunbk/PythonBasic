'''Question: 
Write a Python program to check whether a file exists.
'''

# Python code: 

import os.path
open('abc.txt', 'w')
print(os.path.isfile('abc.txt'))


'''Output sample: 
True
'''