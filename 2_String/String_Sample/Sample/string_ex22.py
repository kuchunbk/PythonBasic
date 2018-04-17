'''Question: 
Write a Python program to sort a string lexicographically.
'''

# Python code: 

def lexicographi_sort(s):
    return sorted(sorted(s), key=str.upper)

print(lexicographi_sort('w3resource'))
print(lexicographi_sort('quickbrown'))


'''Output sample: 
['3', 'c', 'e', 'e', 'o', 'r', 'r', 's', 'u', 'w']                                                            
['b', 'c', 'i', 'k', 'n', 'o', 'q', 'r', 'u', 'w'] 
'''