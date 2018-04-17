'''Question: 
 Write a Python program to create a dictionary from a string.
'''

# Python code: 

from collections import defaultdict, Counter
str1 = 'w3resource' 
my_dict = {}
for letter in str1:
    my_dict[letter] = my_dict.get(letter, 0) + 1
print(my_dict)


'''Output sample: 
{'o': 1, '3': 1, 's': 1, 'r': 2, 'w': 1, 'u': 1, 'e': 2, 'c': 1}
'''