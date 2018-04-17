'''Question: 
Write a Python program using Sieve of Eratosthenes method for computing primes upto a specified number.
'''

# Python code: 

def prime_eratosthenes(n):
    prime_list = []
    for i in range(2, n+1):
        if i not in prime_list:
            print (i)
            for j in range(i*i, n+1, i):
                prime_list.append(j)

print(prime_eratosthenes(100))';


'''Output sample: 
2                                                                                                             
3                                                                                                             
5                                                                                                             
7                                                                                                             
11                                                                                                            
-------
79                                                                                                            
83                                                                                                            
89                                                                                                            
97                                                                                                            
None   
'''