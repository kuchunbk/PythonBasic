'''Question: 
Write a Python program to get unique values from a list.
'''

# Python code: 

my_list = [10, 20, 30, 40, 20, 50, 60, 40]
print("Original List : ",my_list)
my_set = set(my_list)
my_new_list = list(my_set)
print("List of unique numbers : ",my_new_list)


'''Output sample: 
Original List :  [10, 20, 30, 40, 20, 50, 60, 40]                                                             
List of unique numbers :  [40, 10, 50, 20, 60, 30]  
'''