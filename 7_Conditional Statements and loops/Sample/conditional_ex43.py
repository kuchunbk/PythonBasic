'''Question: 
Write a Python program to create the multiplication table (from 1 to 10) of a number.
'''

# Python code: 

n = int(input("Input a number: "))

# use for loop to iterate 10 times
for i in range(1,11):
   print(n,'x',i,'=',n*i)
   

'''Output sample: 
Input a number: 5                                                                                             
5 x 1 = 5                                                                                                     
5 x 2 = 10                                                                                                    
5 x 3 = 15                                                                                                    
5 x 4 = 20                                                                                                    
5 x 5 = 25                                                                                                    
5 x 6 = 30                                                                                                    
5 x 7 = 35                                                                                                    
5 x 8 = 40                                                                                                    
5 x 9 = 45                                                                                                    
5 x 10 = 50 
'''