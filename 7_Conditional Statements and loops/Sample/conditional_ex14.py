'''Question: 
Write a Python program that accepts a string and calculate the number of digits and letters.
'''

# Python code: 

s = input("Input a string")
d=l=0
for c in s:
    if c.isdigit():
        d=d+1
    elif c.isalpha():
        l=l+1
    else:
        pass
print("Letters", l)
print("Digits", d)


'''Output sample: 
Input a string W3resource                                                                                                     
Letters 9                                                                                                                     
Digits 1 
'''