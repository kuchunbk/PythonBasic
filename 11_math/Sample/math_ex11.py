'''Question: 
Write a Python program to calculate the difference between the squared sum of first n natural numbers and the sum of squared first n natural numbers.(default value of number=2).
'''

# Python code: 

def sum_difference(n=2):
    sum_of_squares = 0
    square_of_sum = 0
    for num in range(1, n+1):
        sum_of_squares += num * num
        square_of_sum += num

    square_of_sum = square_of_sum ** 2

    return square_of_sum - sum_of_squares


print(sum_difference(12))


'''Output sample: 
5434
'''