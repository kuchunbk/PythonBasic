'''Question: 
Write a Python program to find missing and additional values in two lists.
'''

# Python code: 

list1 = ['a','b','c','d','e','f']
list2 = ['d','e','f','g','h']
print('Missing values in second list: ', ','.join(set(list1).difference(list2)))
print('Additional values in second list: ', ','.join(set(list2).difference(list1)))


'''Output sample: 
Missing values in second list:  b,c,a                                                                         
Additional values in second list:  g,h 
'''