'''Question: 
Write a Python program to create set difference.
'''

# Python code: 

setx = set(["apple", "mango"])
sety = set(["mango", "orange"])
setz = setx & sety
print(setz)
#Set difference
setb = setx - setz
print(setb)


'''Output sample: 
{'mango'}                                                                                                     
{'apple'} 
'''