'''Question: 
Write a Python program to check if a file path is a file or a directory.
'''

# Python code: 

import os  
path="abc.txt"  
if os.path.isdir(path):  
    print("\nIt is a directory")  
elif os.path.isfile(path):  
    print("\nIt is a normal file")  
else:  
    print("It is a special file (socket, FIFO, device file)" )
print()


'''Output sample: 
It is a normal file  
'''