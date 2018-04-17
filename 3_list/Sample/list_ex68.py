'''Question: 
Write a Python program to extend a list without append.
'''

# Python code: 

x = [10, 20, 30]
y = [40, 50, 60]
x[:0] =y
print(x)


'''Output sample: 
[40, 50, 60, 10, 20, 30] 
'''