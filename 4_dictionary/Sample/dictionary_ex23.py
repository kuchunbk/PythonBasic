'''Question: 
 Write a Python program to combine values in python list of dictionaries.
'''

# Python code: 

from collections import Counter
item_list = [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]
result = Counter()
for d in item_list:
    result[d['item']] += d['amount']
print(result) 


'''Output sample: 
Counter({'item1': 1150, 'item2': 300})
'''