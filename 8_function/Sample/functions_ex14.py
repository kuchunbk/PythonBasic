'''Question: 
Write a Python function to check whether a string is a pangram or not.
'''

# Python code: 

import string, sys
def ispangram(str1, alphabet=string.ascii_lowercase):
    alphaset = set(alphabet)
    return alphaset <= set(str1.lower())
 
print ( ispangram('The quick brown fox jumps over the lazy dog')) 


'''Output sample: 
True
'''