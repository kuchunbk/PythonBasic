'''Question: 
Write a Python program to unpack a tuple in several variables.
'''

# Python code: 

>>> #create a tuple
>>> tuplex = 4, 8, 3 
>>> print(tuplex)
>>> n1, n2, n3 = tuplex
>>> #unpack a tuple in variables
>>> print(n1 + n2 + n3) 
>>> #the number of variables must be equal to the number of items of the tuple
>>> n1, n2, n3, n4 = tuplex 


'''Output sample: 
(4, 8, 3)                                                                                                     
15                                                                                                            
Traceback (most recent call last):                                                                            
  File "32fd05c0-3096-11e7-a6a0-0b37d4d0b2c6.py", line 8, in <module>                                         
    n1, n2, n3, n4 = tuplex                                                                                   
ValueError: not enough values to unpack (expected 4, got 3) 
'''