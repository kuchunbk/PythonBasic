'''Question: 
Write a Python program to assess if a file is closed or not.
'''

# Python code: 

 f = open('abc.txt','r')
print(f.closed)
f.close()
print(f.closed)


'''Output sample: 
False                                                                                                         
True
'''