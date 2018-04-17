'''Question: 
Write a Python program to get the file size of a plain file.
'''

# Python code: 

def file_size(fname):
        import os
        statinfo = os.stat(fname)
        return statinfo.st_size

print("File size in bytes of a plain file: ",file_size("test.txt"))


'''Output sample: 
File size in bytes of a plain file:  151
'''