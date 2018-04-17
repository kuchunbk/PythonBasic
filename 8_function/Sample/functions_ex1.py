'''Question: 
Write a Python function to find the Max of three numbers.
'''

# Python code: 

def max_of_two( x, y ):
    if x > y:
        return x
    return y
def max_of_three( x, y, z ):
    return max_of_two( x, max_of_two( y, z ) )
print(max_of_three(3, 6, -5))


'''Output sample: 
6  
'''