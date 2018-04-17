'''Question: 
Write a Python program to unzip a list of tuples into individual lists.
'''

# Python code: 

>>> #create a tuple
>>> l = [(1,2), (3,4), (8,9)]
>>> printlist((zip(*l)))


'''Output sample: 
[(1, 3, 8), (2, 4, 9)] 
'''