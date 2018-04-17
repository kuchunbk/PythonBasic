'''Question: 
Write apython program to count repeated characters in a string.
'''

# Python code: 

import collections
str1 = 'thequickbrownfoxjumpsoverthelazydog'
d = collections.defaultdict(int)
for c in str1:
    d[c] += 1

for c in sorted(d, key=d.get, reverse=True):
  if d[c] > 1:
      print('%s %d' % (c, d[c]))


'''Output sample: 
o 4                                                                                                           
e 3                                                                                                           
h 2                                                                                                           
t 2                                                                                                           
r 2                                                                                                           
u 2                             
'''