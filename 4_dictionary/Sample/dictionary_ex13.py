'''Question: 
Write a Python program to map two lists into a dictionary.
'''

# Python code: 


keys = ['red', 'green', 'blue']
values = ['#FF0000','#008000', '#0000FF']
color_dictionary = dict(zip(keys, values))
print(color_dictionary)


'''Output sample: 
{'green': '#008000', 'blue': '#0000FF', 'red': '#FF0000'} 
'''