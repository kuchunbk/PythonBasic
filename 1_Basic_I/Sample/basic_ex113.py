'''Question: 
Write a Python program to input a number, if it is not a number generate an error message.
'''

# Python code: 

while True:
    try:
        a = int(input("Input a number: "))
        break
    except ValueError:
        print("\nThis is not a number. Try again...")
        print()
		

'''Output sample: 
Input a  number: abc                                                                                          
                                                                                                              
This is not a number.  Try again...                                                                           
                                                                                                              
Input a  number: 150 
'''