'''Question: 
Sample Solution:- 
'''

# Python code: 

l = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
print([t[:-1] + (100,) for t in l])


'''Output sample: 
[(10, 20, 100), (40, 50, 100), (70, 80, 100)] 
'''