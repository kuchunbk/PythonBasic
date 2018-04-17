'''Question: 
Write a Python program to get the command-line arguments (name of the script, the number of arguments, arguments) passed to a script.
'''

# Python code: 

import sys

print("This is the name/path of the script:"),sys.argv[0]
print("Number of arguments:",len(sys.argv))
print("Argument List:",str(sys.argv))


'''Output sample: 
This is the name/path of the script: test.py
('Number of arguments:', 4)
('Argument List:', "['test.py', 'arg1', 'arg2', 'arg3']")
'''