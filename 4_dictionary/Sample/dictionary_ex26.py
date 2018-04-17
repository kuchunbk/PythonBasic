'''Question: 
 Write a Python program to count the values associated with key in a dictionary.
'''

# Python code: 

student = [{'id': 1, 'success': True, 'name': 'Lary'},
 {'id': 2, 'success': False, 'name': 'Rabi'},
 {'id': 3, 'success': True, 'name': 'Alex'}]
print(sum(d['success'] for d in student))


'''Output sample: 
2  
'''