'''Question: 
Write a Python program to print a specified list after removing the 0th, 4th and 5th elements.
'''

# Python code: 

color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
color = [x for (i,x) in enumerate(color) if i not in (0,4,5)]
print(color)


'''Output sample: 
['Green', 'White', 'Black']
'''