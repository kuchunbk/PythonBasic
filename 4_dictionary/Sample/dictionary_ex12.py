'''Question: 
Write a Python program to remove a key from a dictionary.
'''

# Python code: 

myDict = {'a':1,'b':2,'c':3,'d':4}
print(myDict)
if 'a' in myDict: 
    del myDict['a']
print(myDict)


'''Output sample: 
{'c': 3, 'b': 2, 'd': 4, 'a': 1}                                                                              
{'c': 3, 'b': 2, 'd': 4}
'''