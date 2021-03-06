'''Question: 
Write a Python program to find the index of an item of a tuple.
'''

# Python code: 

>>> #create a tuple
>>> tuplex = tuple("index tuple")
>>> print(tuplex)
>>> #get index of the first item whose value is passed as parameter
>>> index = tuplex.index("p")
>>> print(index)
>>> #define the index from which you want to search
>>> index = tuplex.index("p", 5)
>>> print(index)
>>> #define the segment of the tuple to be searched
>>> index = tuplex.index("e", 3, 6)
>>> print(index)
>>> #if item not exists in the tuple return ValueError Exception
>>> index = tuplex.index("y")


'''Output sample: 
('i', 'n', 'd', 'e', 'x', ' ', 't', 'u', 'p', 'l', 'e')                                                       
8                                                                                                             
8                                                                                                             
3                                                                                                             
Traceback (most recent call last):                                                                            
  File "d0e5ee40-30ab-11e7-a6a0-0b37d4d0b2c6.py", line 14, in <module>                                       
    index = tuplex.index("y")                                                                                 
ValueError: tuple.index(x): x not in tuple   
'''