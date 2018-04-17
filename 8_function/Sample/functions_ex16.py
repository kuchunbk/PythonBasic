'''Question: 
Write a Python function to create and print a list where the values are square of numbers between 1 and 30 (both included).

'''

# Python code: 

def printValues():
	l = list()
	for i in range(1,21):
		l.append(i**2)
	print(l)
		
printValues()


'''Output sample: 
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361, 400]
'''