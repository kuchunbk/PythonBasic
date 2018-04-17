'''Question: 
Write a Python program to print the following floating numbers upto 2 decimal places with a sign.
'''

# Python code: 

x = 3.1415926
y = -12.9999
print("\nOriginal Number: ", x)
print("Formatted Number with sign: "+"{:+.2f}".format(x));
print("Original Number: ", y)
print("Formatted Number with sign: "+"{:+.2f}".format(y));
print()


'''Output sample: 
Original Number:  3.1415926                                                                                   
Formatted Number with sign: +3.14                                                                             
Original Number:  -12.9999                                                                                    
Formatted Number with sign: -13.00
'''