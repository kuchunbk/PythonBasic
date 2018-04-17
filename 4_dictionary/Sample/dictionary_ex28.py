'''Question: 
 Write a Python program to sort a list alphabetically in a dictionary.
'''

# Python code: 

num = {'n1': [2, 3, 1], 'n2': [5, 1, 2], 'n3': [3, 2, 4]}
sorted_dict = {x: sorted(y) for x, y in num.items()}
print(sorted_dict)


'''Output sample: 
{'n1': [1, 2, 3], 'n3': [2, 3, 4], 'n2': [1, 2, 5]}
'''