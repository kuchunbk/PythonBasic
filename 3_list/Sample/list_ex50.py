'''Question: 
Write a Python program to sort a list of nested dictionaries.
'''

# Python code: 

my_list = [{'key': {'subkey': 1}}, {'key': {'subkey': 10}}, {'key': {'subkey': 5}}]
print("Original List: ")
print(my_list)
my_list.sort(key=lambda e: e['key']['subkey'], reverse=True)
print("Sorted List: ")
print(my_list)


'''Output sample: 
Original List:                                                                                                
[{'key': {'subkey': 1}}, {'key': {'subkey': 10}}, {'key': {'subkey': 5}}]                                     
Sorted List:                                                                                                  
[{'key': {'subkey': 10}}, {'key': {'subkey': 5}}, {'key': {'subkey': 1}}]  
'''