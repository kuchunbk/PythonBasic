'''Question: 
Write a Python program to calculate the time runs (difference between start and current time)of a program.
'''

# Python code: 

from timeit import default_timer
def timer(n):
    start = default_timer()
    # some code here
    for row in range(0,n):
        print(row)
    print(default_timer() - start)

timer(5)
timer(15)


'''Output sample: 
0                                                                                                             
1                                                                                                             
2                                                                                                             
3                                                                                                             
4                                                                                                             
2.6107000849151518e-05                                                                                        
0                                                                                                             
1                                                                                                             
2                                                                                                             
3                                                                                                             
4                                                                                                             
5                                                                                                             
6                                                                                                             
7                                                                                                             
8                                                                                                             
9                                                                                                             
10                                                                                                            
11                                                                                                            
12                                                                                                            
13                                                                                                            
14                                                                                                            
4.1371999941475224e-05
'''