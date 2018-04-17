'''Question: 
Write a Python program which accepts a sequence of comma separated 4 digit binary numbers as its input and print the numbers that are divisible by 5 in a comma separated sequence.
'''

# Python code: 

items = []
num = [x for x in input().split(',')]
for p in num:
    x = int(p, 2)
    if not x%5:
        items.append(p)
print(','.join(items))


'''Output sample: 
0001,0010,0011,0100,0101,0110,0111                                                                                            
0101 
'''