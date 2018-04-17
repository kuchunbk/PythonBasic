'''Question: 
Write a Python program to find whether a given number (accept from the user) is even or odd, print out an appropriate message to the user.
'''

# Python code: 

num = int(input("Enter a number: "))
mod = num % 2
if mod > 0:
    print("This is an odd number.")
else:
    print("This is an even number.")

'''Output sample: 
Enter a number: 5                                                                                             
This is an odd number. 
'''