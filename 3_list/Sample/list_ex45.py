'''Question: 
Write a Python program to convert a pair of values into a sorted unique array.
'''

# Python code: 

L = [(1, 2), (3, 4), (1, 2), (5, 6), (7, 8), (1, 2), (3, 4), (3, 4),
 (7, 8), (9, 10)]
print("Original List: ", L)
print("Sorted Unique Data:",sorted(set().union(*L)))


'''Output sample: 
Original List:  [(1, 2), (3, 4), (1, 2), (5, 6), (7, 8), (1, 2), (3, 4), (3, 4), (7, 8), (9, 10)]             
Sorted Unique Data: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  
'''