'''Question: 
Write a Python program to count the frequency of words in a file.
'''

# Python code: 

from collections import Counter
def word_count(fname):
        with open(fname) as f:
                return Counter(f.read().split())

print("Number of words in the file :",word_count("test.txt"))


'''Output sample: 
Number of words in the file : Counter({'this': 7, 'Append': 5, 'text.': 5, 'text.Append': 2, 'Welcome': 1, 'to
': 1, 'w3resource.com.': 1})  
'''