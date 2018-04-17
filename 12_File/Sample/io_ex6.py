'''Question: 
Write a Python program to read a file line by line store it into a variable.
'''

# Python code: 

def file_read(fname):
        with open (fname, "r") as myfile:
                data=myfile.readlines()
                print(data)
file_read('test.txt')


'''Output sample: 
['Welcome to w3resource.com.\n', 'Append this text.Append this text.Append this text.\n', 'Append this text.\n
', 'Append this text.\n', 'Append this text.\n', 'Append this text.\n'] 
'''