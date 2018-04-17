'''Question: 
Write a Python program to determine if variable is defined or not.
'''

# Python code: 

try:
  x = 1
except NameError:
  print("Variable is not defined....!")
else:
  print("Variable is defined.")
try:
  y
except NameError:
  print("Variable is not defined....!")
else:
  print("Variable is defined.")
  

'''Output sample: 
Variable is defined.                                                                                          
Variable is not defined....!
'''