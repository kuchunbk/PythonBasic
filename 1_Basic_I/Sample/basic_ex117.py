'''Question: 
Write a Python program to prove that two string variables of same value point same memory location.
'''

# Python code: 

str1 = "Python"
str2 = "Python"
 
print("\nMemory location of str1 =", hex(id(str1)))
print("Memory location of str2 =", hex(id(str2)))
print()


'''Output sample: 
Memory location of str1 = 0x7f8af3e89f10                                                                      
Memory location of str2 = 0x7f8af3e89f10
'''