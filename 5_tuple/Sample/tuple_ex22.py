'''Question: 
Write a Python program to remove an empty tuple(s) from a list of tuples.
'''

# Python code: 

L = [(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]
L = [t for t in L if t]
print(L)


'''Output sample: 
[('',), ('a', 'b'), ('a', 'b', 'c'), 'd']  
'''