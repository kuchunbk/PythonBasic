'''Question: 
Write a Python program to count the number of characters (character frequency) in a string.
'''

# Python code: 

def char_frequency(str1):
    dict = {}
    for n in str1:
        keys = dict.keys()
        if n in keys:
            dict[n] += 1
        else:
            dict[n] = 1
    return dict
print(char_frequency('google.com'))


'''Output sample: 
{'o': 3, '.': 1, 'g': 2, 'l': 1, 'e': 1, 'c': 1, 'm': 1}
'''