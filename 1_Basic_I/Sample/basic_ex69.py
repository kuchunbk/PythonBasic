'''Question: 
 Write a Python program to sort three integers without using conditional statements and loops.
'''

# Python code: 

x = int(input("Input first number: "))
y = int(input("Input second number: "))
z = int(input("Input third number: "))

a1 = min(x, y, z)
a3 = max(x, y, z)
a2 = (x + y + z) - a1 - a3
print("Numbers in sorted order: ", a1, a2, a3)


'''Output sample: 
Input first number: 2                                                                                         
Input second number: 4                                                                                        
Input third number: 5                                                                                         
Numbers in sorted order:  2 4 5 
'''