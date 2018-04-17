'''Question: 
 Write a Python program to convert height (in feet and inches) to centimeters.
'''

# Python code: 

print("Input your height: ")
h_ft = int(input("Feet: "))
h_inch = int(input("Inches: "))

h_inch += h_ft * 12
h_cm = round(h_inch * 2.54, 1)

print("Your height is : %d cm." % h_cm)


'''Output sample: 
Input your height:                                                                                            
Feet: 5                                                                                                       
Inches: 3                                                                                                     
Your height is : 160 cm. 
'''