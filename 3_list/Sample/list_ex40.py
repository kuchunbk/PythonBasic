'''Question: 
Write a Python program to split a list based on first character of word.
'''

# Python code: 

from itertools import groupby
from operator import itemgetter

word_list = ['be','have','do','say','get','make','go','know','take','see','come','think',
     'look','want','give','use','find','tell','ask','work','seem','feel','leave','call']

for letter, words in groupby(sorted(word_list), key=itemgetter(0)):
    print(letter)
    for word in words:
        print(word)


'''Output sample: 
a                                                                                                             
ask                                                                                                           
b                                                                                                             
be                                                                                                            
c                                                                                                             
call                                                                                                          
come                                                                                                          
d                                                                                                             
do        
-----
w                                                                                                             
want                                                                                                          
work    
'''