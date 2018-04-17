'''Question: 
 Write a Python program to convert a list into a nested dictionary of keys.
'''

# Python code: 

num_list = [1, 2, 3, 4]
new_dict = current = {}
for name in num_list:
    current[name] = {}
    current = current[name]
print(new_dict)


'''Output sample: 
{1: {2: {3: {4: {}}}}}
'''