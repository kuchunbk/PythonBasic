'''Question: 
Write a Python program to convert a tuple to a dictionary.
'''

# Python code: 

>>> #create a tuple
>>> tuplex = ((2, "w"),(3, "r"))
>>> print(dict((y, x) for x, y in tuplex))


'''Output sample: 
{'r': 3, 'w': 2} 
'''