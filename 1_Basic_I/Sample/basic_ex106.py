'''Question: 
Write a Python program to divide a path on the extension separator.
'''

# Python code: 

import os.path
for path in [ 'test.txt', 'filename', '/user/system/test.txt', '/', '' ]:
    print('"%s" :' % path, os.path.splitext(path))
	

'''Output sample: 
"test.txt" : ('test', '.txt')                                      
"filename" : ('filename', '')                                      
"/user/system/test.txt" : ('/user/system/test', '.txt')            
"/" : ('/', '')                                                    
"" : ('', '') 
'''