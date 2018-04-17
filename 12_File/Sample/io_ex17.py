'''Question: 
Write a Python program to remove newline characters from a file.
'''

# Python code: 

def remove_newlines(fname):
    flist = open(fname).readlines()
    return [s.rstrip('\n') for s in flist]

print(remove_newlines("test.txt"))


'''Output sample: 
['Welcome to w3resource.com.', 'Append this text.Append this text.Append this text.', 'Append this text.', 'Ap
pend this text.', 'Append this text.', 'Append this text.'] 
'''