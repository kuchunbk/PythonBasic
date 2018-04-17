'''Question: 
Write a Python program which iterates the integers from 1 to 50. For multiples of three print "Fizz" instead of the number and for the multiples of five print "Buzz". For numbers which are multiples of both three and five print "FizzBuzz".
Sample Solution :- 
Python Code :
for fizzbuzz in range(50):
    if fizzbuzz % 3 == 0 and fizzbuzz % 5 == 0:
        print("fizzbuzz")
        continue
    elif fizzbuzz % 3 == 0:
        print("fizz")
        continue
    elif fizzbuzz % 5 == 0:
        print("buzz")
        continue
    print(fizzbuzz)
	

Sample Output: 
fizzbuzz                                                                                                      
1                                                                                                             
2                                                                                                             
fizz                                                                                                          
4                                                                                                             
buzz                                                                                                          
fizz                                                                                                          
7                                                                                                             
8                                                                                                             
fizz                                                                                                          
buzz                                                                                                          
11          
------
fizzbuzz                                                                                                      
46                                                                                                            
47                                                                                                            
fizz                                                                                                          
49 

Flowchart: 
'''

# Python code: 

for fizzbuzz in range(50):
    if fizzbuzz % 3 == 0 and fizzbuzz % 5 == 0:
        print("fizzbuzz")
        continue
    elif fizzbuzz % 3 == 0:
        print("fizz")
        continue
    elif fizzbuzz % 5 == 0:
        print("buzz")
        continue
    print(fizzbuzz)
	

'''Output sample: 
fizzbuzz                                                                                                      
1                                                                                                             
2                                                                                                             
fizz                                                                                                          
4                                                                                                             
buzz                                                                                                          
fizz                                                                                                          
7                                                                                                             
8                                                                                                             
fizz                                                                                                          
buzz                                                                                                          
11          
------
fizzbuzz                                                                                                      
46                                                                                                            
47                                                                                                            
fizz                                                                                                          
49 
'''