'''Question: 
Write a Python program to format a number with a percentage.
'''

# Python code: 

x = 0.25
y = -0.25
print("\nOriginal Number: ", x)
print("Formatted Number with percentage: "+"{:.2%}".format(x));
print("Original Number: ", y)
print("Formatted Number with percentage: "+"{:.2%}".format(y));
print()


'''Output sample: 
Original Number:  0.25                                                                                        
Formatted Number with percentage: 25.00%                                                                      
Original Number:  -0.25                                                                                       
Formatted Number with percentage: -25.00% 
'''