'''Question: 
Write a Python program to find path refers to a file or directory when you encounter a path name.
'''

# Python code: 

import os.path

for file in [ __file__, os.path.dirname(__file__), '/', './broken_link']:
    print('File        :', file)
    print('Absolute    :', os.path.isabs(file))
    print('Is File?    :', os.path.isfile(file))
    print('Is Dir?     :', os.path.isdir(file))
    print('Is Link?    :', os.path.islink(file))
    print('Exists?     :', os.path.exists(file))
    print('Link Exists?:', os.path.lexists(file))
	

'''Output sample: 
File        : 26cb6a20-266f-11e7-a9c1-cf681af3cdf1.py              
Absolute    : False                                                
Is File?    : True                                                 
Is Dir?     : False                                                
Is Link?    : False                                                
Exists?     : True                                                 
Link Exists?: True  
------
Is Dir?     : False                                                
Is Link?    : False                                                
Exists?     : False                                                
Link Exists?: False 
'''