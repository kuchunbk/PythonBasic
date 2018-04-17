'''Question: 
Write a Python program to split a list every Nth element.
'''

# Python code: 

C = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n']
def list_slice(S, step):
    return [S[i::step] for i in range(step)]
print(list_slice(C,3))


'''Output sample: 
[['a', 'd', 'g', 'j', 'm'], ['b', 'e', 'h', 'k', 'n'], ['c', 'f', 'i', 'l']] 
'''