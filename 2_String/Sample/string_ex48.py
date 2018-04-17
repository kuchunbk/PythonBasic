'''Question: 
Write a Python program to swap comma and dot in a string.
'''

# Python code: 

amount = "32.054,23"
maketrans = amount.maketrans
amount = amount.translate(maketrans(',.', '.,'))
print(amount)


'''Output sample: 
32,054.23                  
'''