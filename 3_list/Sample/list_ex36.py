'''Question: 
Write a Python program to get variable unique identification number or string. 
'''

# Python code: 

x = 100
print(format(id(x), 'x'))
s = 'w3resource'
print(format(id(s), 'x')) 


'''Output sample: 
a6aa40                                                                 
7f209e6c6670   
'''