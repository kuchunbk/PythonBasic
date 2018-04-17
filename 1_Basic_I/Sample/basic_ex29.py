'''Question: 
Write a Python program to print out a set containing all the colors from a list which are not present in another list 
'''

# Python code: 

color_list_1 = set(["White", "Black", "Red"])
color_list_2 = set(["Red", "Green"])

print(color_list_1.difference(color_list_2))


'''Output sample: 
{'White', 'Black'} 
'''