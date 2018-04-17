'''Question: 
Write a Python program to get the actual module object for a given object.
'''

# Python code: 

from inspect import getmodule
from math import sqrt
print(getmodule(sqrt))


'''Output sample: 
<module 'math' (built-in)>
'''