'''Question: 
Write a Python program to test if a certain number is greater than all numbers of a list.
'''

# Python code: 

num = [2,3,4]
print()
print(all(x > 1 for x in num))
print(all(x > 4 for x in num))
print()


'''Output sample: 
True                                                                                                          
False 
'''