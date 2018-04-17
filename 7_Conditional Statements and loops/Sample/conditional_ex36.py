'''Question: 
Write a Python program to check a triangle is equilateral, isosceles or scalene.
Note :
An equilateral triangle is a triangle in which all three sides are equal.
A scalene triangle is a triangle that has three unequal sides.
An isosceles triangle is a triangle with (at least) two equal sides.
'''

# Python code: 

print("Input lengths of the triangle sides: ")
x = int(input("x: "))
y = int(input("y: "))
z = int(input("z: "))

if x == y == z:
	print("Equilateral triangle")
elif x != y != z:
	print("Scalene triangle")
else:
	print("isosceles triangle") 
	

'''Output sample: 
x: 6                                                                                                          
y: 8                                                                                                          
z: 12                                                                                                         
Scalene triangle  
'''