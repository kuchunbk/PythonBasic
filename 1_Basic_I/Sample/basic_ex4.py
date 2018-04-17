'''Question: 
Write a Python program which accepts the radius of a circle from the user and compute the area.
'''

# Python code: 

from math import pi
r = float(input ("Input the radius of the circle : "))
print ("The area of the circle with radius " + str(r) + " is: " + str(pi * r**2))


'''Output sample: 
Input the radius of the circle : 1.1                                                                          
The area of the circle with radius 1.1 is: 3.8013271108436504 
'''