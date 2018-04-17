'''Question: 
Write a Python program to create a copy of its own source code.
'''

# Python code: 

print()
print((lambda str='print(lambda str=%r: (str %% str))()': (str % str))())
print()


'''Output sample: 
print(lambda str='print(lambda str=%r: (str %% str))()': (str % str))()
'''