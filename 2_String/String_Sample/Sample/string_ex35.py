'''Question: 
Write a Python program to display a number with a comma separator.
'''

# Python code: 

x = 3000000
y = 30000000
print("\nOriginal Number: ", x)
print("Formatted Number with comma separator: "+"{:,}".format(x));
print("Original Number: ", y)
print("Formatted Number with comma separator: "+"{:,}".format(y));
print()


'''Output sample: 
Original Number:  3000000                                                                                     
Formatted Number with comma separator: 3,000,000                                                              
Original Number:  30000000                                                                                    
Formatted Number with comma separator: 30,000,000 
'''