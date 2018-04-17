'''Question: 
Write a Python program to find a tuple, the smallest second index value from a list of tuples.
'''

# Python code: 

x = [(4, 1), (1, 2), (6, 0)]
print(min(x, key=lambda n: (n[1], -n[0])))


'''Output sample: 
(6, 0) 
'''