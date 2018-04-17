'''Question: 
Write a Python program to get the maximum and minimum value in a dictionary.
'''

# Python code: 

my_dict = {'x':500, 'y':5874, 'z': 560}

key_max = max(my_dict.keys(), key=(lambda k: my_dict[k]))
key_min = min(my_dict.keys(), key=(lambda k: my_dict[k]))

print('Maximum Value: ',my_dict[key_max])
print('Minimum Value: ',my_dict[key_min])


'''Output sample: 
Maximum Value:  5874                                                                                          
Minimum Value:  500
'''