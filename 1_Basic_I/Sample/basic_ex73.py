'''Question: 
Write a Python program to calculate midpoints of a line.
'''

# Python code: 

print('\nCalculate the midpoint of a line :')

x1 = float(input('The value of x (the first endpoint) '))
y1 = float(input('The value of y (the first endpoint) '))

x2 = float(input('The value of x (the first endpoint) '))
y2 = float(input('The value of y (the first endpoint) '))

x_m_point = (x1 + x2)/2
y_m_point = (y1 + y2)/2
print();
print("The midpoint of line is :")
print( "The midpoint's x value is: ",x_m_point)
print( "The midpoint's y value is: ",y_m_point)
print();


'''Output sample: 
Calculate the midpoint of a line :                                                                            
The value of x (the first endpoint) 2                                                                         
The value of y (the first endpoint) 2                                                                         
The value of x (the first endpoint) 4                                                                         
The value of y (the first endpoint) 4                                                                         
                                                                                                              
The midpoint of line is :                                                                                     
The midpoint's x value is:  3.0                                                                               
The midpoint's y value is:  3.0 
'''