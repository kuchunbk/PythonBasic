'''Question: 
Write a Python program to get a string which is n (non-negative integer) copies of a given string.
'''

# Python code: 

def larger_string(str, n):
   result = ""
   for i in range(n):
      result = result + str
   return result

print(larger_string('abc', 2))
print(larger_string('.py', 3))


'''Output sample: 
abcabc                                                                                                        
.py.py.py 
'''