'''Question: 
Write a Python program which accepts a sequence of comma-separated numbers from user and generate a list and a tuple with those numbers. 
'''

# Python code: 

values = input("Input some comma seprated numbers : ")
list = values.split(",")
tuple = tuple(list)
print('List : ',list)
print('Tuple : ',tuple)


'''Output sample: 
Input some comma seprated numbers : 3,5,7,23                       
List :  ['3', '5', '7', '23']                                      
Tuple :  ('3', '5', '7', '23')          
'''