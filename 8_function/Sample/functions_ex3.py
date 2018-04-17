'''Question: 
Write a Python function to multiply all the numbers in a list.
'''

# Python code: 

def multiply(numbers):  
    total = 1
    for x in numbers:
        total *= x  
    return total  
print(multiply((8, 2, 3, -1, 7)))


'''Output sample: 
-336 
'''