'''Question: 
Write a Python program to multiplies all the items in a list.
'''

# Python code: 

def multiply_list(items):
    tot = 1
    for x in items:
        tot *= x
    return tot
print(multiply_list([1,2,-8]))


'''Output sample: 
-16
'''