'''Question: 
Write a Python program to guess a number between 1 to 9.
'''

# Python code: 

import random
target_num, guess_num = random.randint(1, 10), 0
while target_num != guess_num:
    guess_num = int(input('Guess a number between 1 and 10 until you get it right : '))
print('Well guessed!')


'''Output sample: 
Guess a number between 1 and 10 until you get it right : 5                                                    
Well guessed!  
'''