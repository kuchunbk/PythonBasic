'''Question: 
Write a Python program to generate groups of five consecutive numbers in a list.
'''

# Python code: 

l = [[5*i + j for j in range(1,6)] for i in range(5)]
print(l)


'''Output sample: 
[[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20], [21, 22, 23, 24, 25]]  
'''