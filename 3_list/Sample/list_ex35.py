'''Question: 
Write a Python program to create a list by concatenating a given list which range goes from 1 to n. 
'''

# Python code: 

my_list = ['p', 'q']
n = 4
new_list = ['{}{}'.format(x, y) for y in range(1, n+1) for x in my_list]
print(new_list)


'''Output sample: 
['p1', 'q1', 'p2', 'q2', 'p3', 'q3', 'p4', 'q4'] 
'''