'''Question: 
 Write a Python program to match key values in two dictionaries.
'''

# Python code: 

x = {'key1': 1, 'key2': 3, 'key3': 2}
y = {'key1': 1, 'key2': 2}
for (key, value) in set(x.items()) & set(y.items()):
    print('%s: %s is present in both x and y' % (key, value))
	

'''Output sample: 
key1: 1 is present in both x and y 
'''