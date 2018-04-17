'''Question: 
Write a Python program to find the median of three values.
'''

# Python code: 

a = float(input("Input first number: "))
b = float(input("Input second number: "))
c = float(input("Input third number: "))
if a > b:
    if a < c:
        median = a
    elif b > c:
        median = b
    else:
        median = c
else:
    if a > c:
        median = a
    elif b < c:
        median = b
    else:
        median = c

print("The median is", median)


'''Output sample: 
Input first number: 25                                                                                        
Input second number: 55                                                                                       
Input third number: 65                                                                                        
The median is 55.0 
'''