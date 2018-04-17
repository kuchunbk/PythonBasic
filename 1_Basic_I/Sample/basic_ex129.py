'''Question: 
Write a Python program to add leading zeroes to a string.
'''

# Python code: 

str1='122.22'
print("Original String: ",str1)
str1 = str1.ljust(8, '0')
print(str1)
str1 = str1.ljust(10, '0')
print(str1)


'''Output sample: 
Original String:  122.22                                                                                      
122.2200                                                                                                      
122.220000
'''