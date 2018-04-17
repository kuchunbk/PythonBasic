'''Question: 
 Write a Python program to print a dictionary in table format.
'''

# Python code: 

my_dict = {'C1':[1,2,3],'C2':[5,6,7],'C3':[9,10,11]}
for row in zip(*([key] + (value) for key, value in sorted(my_dict.items()))):
    print(*row)
	

'''Output sample: 
C1 C2 C3                                                                                                      
1 5 9                                                                                                         
2 6 10                                                                                                        
3 7 11
'''