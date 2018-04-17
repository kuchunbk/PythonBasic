'''Question: 
Write a Python program to calculate the sum of all digits of the base to the specified power.
'''

# Python code: 

def power_base_sum(base, power):
    return sum([int(i) for i in str(pow(base, power))])


print(power_base_sum(2, 100))
print(power_base_sum(8, 10))


'''Output sample: 
115                                                                                                           
37 
'''