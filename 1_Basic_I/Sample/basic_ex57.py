'''Question: 
 Write a program to get execution time (in seconds) for a Python method.
'''

# Python code: 

import time
def sum_of_n_numbers(n):
    start_time = time.time()
    s = 0
    for i in range(1,n+1):
        s = s + i
    end_time = time.time()
    return s,end_time-start_time

n = 5
print("\nTime to sum of 1 to ",n," and required time to calculate is :",sum_of_n_numbers(n))


'''Output sample: 
Time to sum of 1 to  5  and required time to calculate is : (15, 2.384185791015625e-06) 
'''