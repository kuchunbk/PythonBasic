'''Question: 
Write a Python program to create a shallow copy of sets.
'''

# Python code: 

setp = set(["Red", "Green"])
setq = set(["Green", "Red"])
#A shallow copy
setr = setp.copy()
print(setr)


'''Output sample: 
{'Red', 'Green'}
'''