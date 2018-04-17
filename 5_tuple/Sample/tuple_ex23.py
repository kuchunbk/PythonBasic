'''Question: 
Write a Python program to sort a tuple by its float element.
'''

# Python code: 

price = [('item1', '12.20'), ('item2', '15.10'), ('item3', '24.5')]
print( sorted(price, key=lambda x: float(x[1]), reverse=True))


'''Output sample: 
[('item3', '24.5'), ('item2', '15.10'), ('item1', '12.20')] 
'''