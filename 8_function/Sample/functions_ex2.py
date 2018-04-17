'''Question: 
Write a Python function to sum all the numbers in a list.
'''

# Python code: 

def sum(numbers):
    total = 0
    for x in numbers:
        total += x
    return total
print(sum((8, 2, 3, 0, 7)))


'''Output sample: 
20
'''