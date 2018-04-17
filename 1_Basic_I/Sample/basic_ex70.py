'''Question: 
 Write a Python program to sort files by date.
'''

# Python code: 

import glob
import os

files = glob.glob("*.txt")
files.sort(key=os.path.getmtime)
print("\n".join(files))


'''Output sample: 
result.txt                                                                                                    
temp.txt                                                                                                      
myfile.txt                                                                                                    
mynewtest.txt                                                                                                 
mytest.txt                                                                                                    
abc.txt                                                                                                       
test.txt 
'''