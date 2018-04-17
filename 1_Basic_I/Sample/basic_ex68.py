'''Question: 
 Write a Python program to calculate the sum of the digits in an integer.
'''

# Python code: 

num = int(input("Input a four digit numbers: "))
x  = num //1000
x1 = (num - x*1000)//100
x2 = (num - x*1000 - x1*100)//10
x3 = num - x*1000 - x1*100 - x2*10
print("The sum of digits in the number is", x+x1+x2+x3)


'''Output sample: 
Input a four digit numbers: 5245                                                                              
The sum of digits in the number is 16
'''