'''Question: 
Write a Python program to add member(s) in a set.
'''

# Python code: 

#A new empty set
color_set = set()
color_set.add("Red")
print(color_set)
#Add multiple items
color_set.update(["Blue", "Green"])
print(color_set)


'''Output sample: 
{'Red'}                                                                                                       
{'Red', 'Blue', 'Green'}
'''