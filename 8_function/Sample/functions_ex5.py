'''Question: 
Write a Python function to calculate the factorial of a number (a non-negative integer). The function accepts the number as an argument.
'''

# Python code: 

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
n=int(input("Input a number to compute the factiorial : "))
print(factorial(n))


'''Output sample: 
Input a number to compute the factiorial : 4                                                                  
24
'''