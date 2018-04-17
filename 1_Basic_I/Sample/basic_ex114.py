'''Question: 
Write a Python program to filter the positive numbers from a list.
'''

# Python code: 

nums = [34, 1, 0, -23]
print("Original numbers in the list: ",nums)
new_nums = list(filter(lambda x: x >0, nums))
print("Positive numbers in the list: ",new_nums)


'''Output sample: 
Original numbers in the list:  [34, 1, 0, -23]                                                                
Positive numbers in the list:  [34, 1]
'''