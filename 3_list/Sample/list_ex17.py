'''Question: 
Write a Python program to generate and print a list except for the first 5 elements, where the values are square of numbers between 1 and 30 (both included).
'''

# Python code: 

def printValues():
	l = list()
	for i in range(1,21):
		l.append(i**2)
	print(l[5:])

printValues()


'''Output sample: 
[36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361, 400]
'''