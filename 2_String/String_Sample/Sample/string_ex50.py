'''Question: 
Write a Python program to split a string on the last occurrence of the delimiter.
'''

# Python code: 

str1 = "w,3,r,e,s,o,u,r,c,e"
print(str1.rsplit(',', 1))
print(str1.rsplit(',', 2))
print(str1.rsplit(',', 5))


'''Output sample: 
['w,3,r,e,s,o,u,r,c', 'e']                                                                                    
['w,3,r,e,s,o,u,r', 'c', 'e']                                                                                 
['w,3,r,e,s', 'o', 'u', 'r', 'c', 'e']               
'''