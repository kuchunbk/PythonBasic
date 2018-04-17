'''Question: 
Write a Python program to read an entire text file.
'''

# Python code: 

def file_read(fname):
        txt = open(fname)
        print(txt.read())

file_read('test.txt')


'''Output sample: 
Welcome to w3resource.com.                                                                                    
Append this text.Append this text.Append this text.                                                           
Append this text.                                                                                             
Append this text.                                                                                             
Append this text.                                                                                             
Append this text. 
'''