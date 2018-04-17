'''Question: 
Write a Python program to check if a string contains all letters of the alphabet.
'''

# Python code: 

import string
alphabet = set(string.ascii_lowercase)
input_string = 'The quick brown fox jumps over the lazy dog'
print(set(input_string.lower()) >= alphabet)
input_string = 'The quick brown fox jumps over the lazy cat'
print(set(input_string.lower()) >= alphabet)


'''Output sample: 
True                                                                                                          
False                        
'''