'''Question: 
Write a Python program to create a symmetric difference.
'''

# Python code: 


setx = set(["apple", "mango"])
sety = set(["mango", "orange"])
#Symmetric difference
setc = setx ^ sety
print(setc)


'''Output sample: 
{'apple', 'orange'}
'''