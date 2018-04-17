'''Question: 
 Write a Python program to calculate the hypotenuse of a right angled triangle.
'''

# Python code: 

from math import sqrt
print("Input lengths of shorter triangle sides:")
a = float(input("a: "))
b = float(input("b: "))

c = sqrt(a**2 + b**2)
print("The length of the hypotenuse is", c )


'''Output sample: 
Input lengths of shorter triangle sides:                                                                      
a: 3                                                                                                          
b: 4                                                                                                          
The length of the hypotenuse is 5.0  
'''