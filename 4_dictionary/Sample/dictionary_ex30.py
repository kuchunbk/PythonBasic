'''Question: 
 Write a Python program to get the top three items in a shop.
'''

# Python code: 

from heapq import nlargest
from operator import itemgetter
items = {'item1': 45.50, 'item2':35, 'item3': 41.30, 'item4':55, 'item5': 24}
for name, value in nlargest(3, items.items(), key=itemgetter(1)):
    print(name, value)
	

'''Output sample: 
item4 55                                                                                                      
item1 45.5                                                                                                    
item3 41.3 
'''