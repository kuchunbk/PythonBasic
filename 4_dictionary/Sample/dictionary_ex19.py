'''Question: 
 Write a Python program to combine two dictionary adding values for common keys.
'''

# Python code: 

from collections import Counter
d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}
d = Counter(d1) + Counter(d2)
print(d)


'''Output sample: 
Counter({'b': 400, 'd': 400, 'a': 400, 'c': 300}) 
'''