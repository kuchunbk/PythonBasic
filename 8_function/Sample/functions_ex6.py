'''Question: 
Write a Python function to check whether a number is in a given range.
'''

# Python code: 

def test_range(n):
    if n in range(3,9):
        print( " %s is in the range"%str(n))
    else :
        print("The number is outside the given range.")
test_range(5)


'''Output sample: 
 5 is in the range
 '''