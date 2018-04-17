'''Question: 
Write a Python function that that prints out the first n rows of Pascal's triangle.
'''

# Python code: 

def pascal_triangle(n):
   trow = [1]
   y = [0]
   for x in range(max(n,0)):
      print(trow)
      trow=[l+r for l,r in zip(trow+y, y+trow)]
   return n>=1
pascal_triangle(6) 


'''Output sample: 
[1]                                                                                                           
[1, 1]                                                                                                        
[1, 2, 1]                                                                                                     
[1, 3, 3, 1]                                                                                                  
[1, 4, 6, 4, 1]                                                                                               
[1, 5, 10, 10, 5, 1]  
'''