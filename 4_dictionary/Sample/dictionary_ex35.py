'''Question: 
 Write a Python program to sort Counter by value.
'''

# Python code: 

from collections import Counter
x = Counter({'Math':81, 'Physics':83, 'Chemistry':87})
print(x.most_common())


'''Output sample: 
[('Chemistry', 87), ('Physics', 83), ('Math', 81)]
'''