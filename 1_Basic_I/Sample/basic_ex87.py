'''Question: 
Write a Python program to get the size of a file.
'''

# Python code: 

import os
file_size = os.path.getsize("abc.txt")
print("\nThe size of abc.txt is :",file_size,"Bytes")
print()


'''Output sample: 
The size of abc.txt is : 0 Bytes
'''