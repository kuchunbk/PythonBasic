'''Question: 
Write a Python program to check if an integer fits in 64 bits.
'''

# Python code: 

int_val = 30
if int_val.bit_length() <= 63:
    print((-2 ** 63).bit_length())
    print((2 ** 63).bit_length())
	

'''Output sample: 
64                                                                                                            
64 
'''