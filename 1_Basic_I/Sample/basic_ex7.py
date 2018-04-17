'''Question: 
Write a Python program to accept a filename from the user and print the extension of that.
'''

# Python code: 

filename = input("Input the Filename: ")
f_extns = filename.split(".")
print ("The extension of the file is : " + repr(f_extns[-1]))


'''Output sample: 
Input the Filename: abc.java                                                                                  
The  extension of the file is : 'java'
'''