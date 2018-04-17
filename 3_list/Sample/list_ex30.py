'''Question: 
Write a Python program to get the frequency of the elements in a list.
'''

# Python code: 

import collections
my_list = [10,10,10,10,20,20,20,20,40,40,50,50,30]
print("Original List : ",my_list)
ctr = collections.Counter(my_list)
print("Frequency of the elements in the List : ",ctr)


'''Output sample: 
Original List :  [10, 10, 10, 10, 20, 20, 20, 20, 40, 40, 50, 50, 30]                                         
Frequency of the elements in the List :  Counter({10: 4, 20: 4, 40: 2, 50: 2, 30: 1}) 
'''