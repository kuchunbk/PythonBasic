'''Question: 
 Write a Python program to count number of items in a dictionary value that is a list.
'''

# Python code: 

dict =  {'Alex': ['subj1', 'subj2', 'subj3'], 'David': ['subj1', 'subj2']}
ctr = sum(map(len, dict.values()))
print(ctr)


'''Output sample: 
5
'''