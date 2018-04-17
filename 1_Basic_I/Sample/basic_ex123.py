'''Question: 
Write a Python program to determine the largest and smallest integers, longs, floats.
'''

# Python code: 

import sys
print("Float value information: ",sys.float_info)
print("\nInteger value information: ",sys.int_info)
print("\nMaximum size of an integer: ",sys.maxsize) 


'''Output sample: 
Float value information: sys.float_info(max=1.7976931348623157e+308, max_exp=1024, max_10_exp=308, min=2.2250
738585072014e-308, min_exp=-1021, min_10_exp=-307, dig=15, mant_dig=53, epsilon=2.220446049250313e-16, radix=2
, rounds=1)                                                                                                   
                                                                                                              
Integer value information: sys.int_info(bits_per_digit=30, sizeof_digit=4)                                   
                                                                                                              
Maximum size of an integer: 9223372036854775807  
'''