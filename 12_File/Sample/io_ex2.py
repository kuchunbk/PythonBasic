'''Question: 
Write a Python program to read first n lines of a file.
'''

# Python code: 

def file_read_from_head(fname, nlines):
        from itertools import islice
        with open(fname) as f:
                for line in islice(f, nlines):
                        print(line)
file_read_from_head('test.txt',2)


'''Output sample: 
Welcome to w3resource.com.                                                                                    
                                                                                                              
Append this text.Append this text.Append this text. 
'''