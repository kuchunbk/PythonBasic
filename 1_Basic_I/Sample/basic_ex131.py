'''Question: 
Write a Python program to split a variable length string into variables.
'''

# Python code: 

var_list = ['a', 'b', 'c']
x, y, z = (var_list + [None] * 3)[:3]
print(x, y, z)
var_list = [100, 20.25]
x, y = (var_list + [None] * 2)[:2]
print(x, y)


'''Output sample: 
a b c                                                                                                         
100 20.25 
'''