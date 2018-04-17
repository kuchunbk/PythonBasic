'''Question: 
Write a Python program to display a number in left, right and center aligned of width 10.
'''

# Python code: 

x = 22
print("\nOriginal Number: ", x)
print("Left aligned (width 10)   :"+"{:< 10d}".format(x));
print("Right aligned (width 10)  :"+"{:10d}".format(x));
print("Center aligned (width 10) :"+"{:^10d}".format(x));
print()


'''Output sample: 
Original Number:  22                                                                                          
Left aligned (width 10)   :22                                                                                 
Right aligned (width 10)  :        22                                                                         
Center aligned (width 10) :    22  
'''