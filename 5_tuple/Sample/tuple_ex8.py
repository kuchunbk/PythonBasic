'''Question: 
Write a Python program to create the colon of a tuple.
'''

# Python code: 

>>> from copy import deepcopy
>>> #create a tuple
>>> tuplex = ("HELLO", 5, [], True) 
>>> print(tuplex)
>>> #make a copy of a tuple using deepcopy() function
>>> tuplex_clone = deepcopy(tuplex)
>>> tuplex_clone[2].append(50)
>>> print(tuplex_clone)
>>> print(tuplex)
>>>


'''Output sample: 
('HELLO', 5, [], True)                                                                                        
('HELLO', 5, [50], True)                                                                                      
('HELLO', 5, [], True) 
'''