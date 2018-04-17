'''Question: 
Write a Python program to print the current call stack.
'''

# Python code: 

import traceback
print()
def f1():return abc()
def abc():traceback.print_stack()
f1()
print()


'''Output sample: 
File "7a070e70-25c4-11e7-bc90-3fdc1ec1c64d.py", line 5, in                                          
    f1()                                                                                                      
  File "7a070e70-25c4-11e7-bc90-3fdc1ec1c64d.py", line 3, in f1                                               
    def f1():return abc()                                                                                     
  File "7a070e70-25c4-11e7-bc90-3fdc1ec1c64d.py", line 4, in abc                                              
    def abc():traceback.print_stack() 
	'''