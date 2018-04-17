'''Question: 
Write a Python program to check if all items of a list is equal to a given string.
'''

# Python code: 


color1 = ["green", "orange", "black", "white"]
color2 = ["green", "green", "green", "green"]

print(all(c == 'blue' for c in color1))
print(all(c == 'green' for c in color2))


'''Output sample: 
False                                                                                                         
True
'''