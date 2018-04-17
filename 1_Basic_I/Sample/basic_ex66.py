'''Question: 
 Write a Python program to calculate body mass index.
'''

# Python code: 

height = float(input("Input your height in meters: "))
weight = float(input("Input your weight in kilogram: "))
print("Your body mass index is: ", round(weight / (height * height), 2))


'''Output sample: 
Input your height in meters: 5.8                                                                              
Input your weight in kilogram: 85                                                                             
Your body mass index is:  2.53 
'''