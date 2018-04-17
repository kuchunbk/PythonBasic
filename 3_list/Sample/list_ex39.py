'''Question: 
Write a Python program to convert a list of multiple integers into a single integer.
'''

# Python code: 

L = [11, 33, 50]
print("Original List: ",L)
x = int("".join(map(str, L)))
print("Single Integer: ",x)


'''Output sample: 
Original List:  [11, 33, 50]                                                                                  
Single Integer:  113350
'''