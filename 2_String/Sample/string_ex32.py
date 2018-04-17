'''Question: 
Write a Python program to print the following floating numbers with no decimal places.
'''

# Python code: 

x = 3.1415926
y = -12.9999
print("\nOriginal Number: ", x)
print("Formatted Number with no decimal places: "+"{:.0f}".format(x));
print("Original Number: ", y)
print("Formatted Number with no decimal places: "+"{:.0f}".format(y));
print()


'''Output sample: 
Original Number:  3.1415926                                                                                   
Formatted Number with no decimal places: 3                                                                    
Original Number:  -12.9999                                                                                    
Formatted Number with no decimal places: -13 
'''