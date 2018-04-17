'''Question: 
Write a Python program to write a list content to a file.
'''

# Python code: 

color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
with open('abc.txt', "w") as myfile:
        for c in color:
                myfile.write("%s\n" % c)

content = open('abc.txt')
print(content.read())


'''Output sample: 
Red                                                                                                           
Green                                                                                                         
White                                                                                                         
Black                                                                                                         
Pink                                                                                                          
Yellow
'''