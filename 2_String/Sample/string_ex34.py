'''Question: 
Write a Python program to print the following integers with '*' on the right of specified width.
'''

# Python code: 

x = 3
y = 123
print("\nOriginal Number: ", x)
print("Formatted Number(right padding, width 2): "+"{:*< 2d}".format(x));
print("Original Number: ", y)
print("Formatted Number(right padding, width 6): "+"{:*< 6d}".format(y));
print()


'''Output sample: 
Original Number:  3                                                                                           
Formatted Number(right padding, width 2): 3*                                                                  
Original Number:  123                                                                                         
Formatted Number(right padding, width 6): 123*** 
'''