'''Question: 
Write a Python program to convert a list of tuples into a dictionary.
'''

# Python code: 

>>> #create a list
>>> l = [("x", 1), ("x", 2), ("x", 3), ("y", 1), ("y", 2), ("z", 1)]
>>> d = {}
>>> for a, b in l:
>>>     d.setdefault(a, []).append(b)
>>> print (d)


'''Output sample: 
{'y': [1, 2], 'z': [1], 'x': [1, 2, 3]} 
'''