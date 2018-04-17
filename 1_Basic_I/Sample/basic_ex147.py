'''Question: 
Write a Python function to test if a number n is multiply by another number m. Accept two integers values form the user.
'''

# Python code: 

def multiple(m, n):
	return True if m % n == 0 else False

print(multiple(20, 5))
print(multiple(7, 2))


'''Output sample: 
True
False
'''