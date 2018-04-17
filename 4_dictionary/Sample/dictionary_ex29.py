'''Question: 
 Write a Python program to remove spaces from dictionary keys.
'''

# Python code: 

student_list = {'S  001': ['Math', 'Science'], 'S    002': ['Math', 'English']}
print("Original dictionary: ",student_list)
student_dict = {x.translate({32: None}): y for x, y in student_list.items()}
print("New dictionary: ",student_dict)


'''Output sample: 
Original dictionary:  {'S    002': ['Math', 'English'], 'S  001': ['Math', 'Science']}                        
New dictionary:  {'S    002': ['Math', 'English'], 'S  001': ['Math', 'Science']} 
'''