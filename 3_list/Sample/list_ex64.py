'''Question: 
Write a Python program to iterate over two lists simultaneously.
'''

# Python code: 

num = [1, 2, 3]
color = ['red', 'while', 'black']
for (a,b) in zip(num, color):
     print(a, b)
	 

'''Output sample: 
1 red                                                                                                         
2 while                                                                                                       
3 black
'''