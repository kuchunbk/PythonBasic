'''Question: 
Write a Python program to create a union of sets.
'''

# Python code: 

#Union
setx = set(["green", "blue"])
sety = set(["blue", "yellow"])
seta = setx | sety
print(seta)


'''Output sample: 
{'yellow', 'green', 'blue'} 
'''