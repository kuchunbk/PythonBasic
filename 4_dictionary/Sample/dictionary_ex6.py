'''Question: 
Write a Python script to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x).
'''

# Python code: 

n=int(input("Input a number "))
d = dict()

for x in range(1,n+1):
    d[x]=x*x

print(d) 


'''Output sample: 
10                                                                                                            
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100}   
'''