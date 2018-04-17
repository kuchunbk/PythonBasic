'''Question: 
Write a Python program to find common items from two lists. 
'''

# Python code: 

color1 = "Red", "Green", "Orange", "White"
color2 = "Black", "Green", "White", "Pink"
print(set(color1) & set(color2))


'''Output sample: 
{'Green', 'White'} 
'''