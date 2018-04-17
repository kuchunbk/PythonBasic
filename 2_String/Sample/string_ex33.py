'''Question: 
Write a Python program to print the following integers with zeros on the left of specified width.
'''

# Python code: 

x = 3
y = 123
print("\nOriginal Number: ", x)
print("Formatted Number(left padding, width 2): "+"{:0>2d}".format(x));
print("Original Number: ", y)
print("Formatted Number(left padding, width 6): "+"{:0>6d}".format(y));
print()


'''Output sample: 

Original Number:  3                                                                                           
Formatted Number(left padding, width 2): 03                                                                   
Original Number:  123                                                                                         
Formatted Number(left padding, width 6): 000123 
'''