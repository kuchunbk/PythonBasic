'''Question: 
Write a Python program to returns sum of all divisors of a number.
'''

# Python code: 

def sum_div(number):
    divisors = [1]
    for i in range(2, number):
        if (number % i)==0:
            divisors.append(i)
    return divisors
print(sum_div(8))
print(sum_div(12))


'''Output sample: 
[1, 2, 4]                                                                                                     
[1, 2, 3, 4, 6]
'''