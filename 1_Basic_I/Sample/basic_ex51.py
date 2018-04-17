'''Question: 
 Write a Python program to determine profiling of Python programs.
'''

# Python code: 

import cProfile
def sum():
    print(1+2)
cProfile.run('sum()')


'''Output sample: 
3                                                                                                             
         5 function calls in 0.000 seconds                                                                    
                                                                                                              
   Ordered by: standard name                                                                                  
                                                                                                              
   ncalls  tottime  percall  cumtime  percall filename:lineno(function)                                       
        1    0.000    0.000    0.000    0.000 7aa14930-2430-11e7-807b-bd9de91b1602.py:2(sum)                  
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)                                            
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}                                 
        1    0.000    0.000    0.000    0.000 {built-in method builtins.print}                                
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}  
	'''