'''Question: 
Write a Python program to iterate over dictionaries using for loops.
'''

# Python code: 

d = {'Red': 1, 'Green': 2, 'Blue': 3} 
for color_key, value in d.items():
     print(color_key, 'corresponds to ', d[color_key]) 


'''Output sample: 
Red corresponds to  1                                                                                         
Blue corresponds to  3                                                                                        
Green corresponds to  2 
'''