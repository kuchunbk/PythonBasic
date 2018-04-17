'''Question: 
Write a Python program to strip a set of characters from a string.
'''

# Python code: 

def strip_chars(str, chars):
    return "".join(c for c in str if c not in chars)

print("\nOriginal String: ")
print("The quick brown fox jumps over the lazy dog.")
print("After stripping a,e,i,o,u")      
print(strip_chars("The quick brown fox jumps over the lazy dog.", "aeiou"))
print()


'''Output sample: 
Original String:                                                                                              
The quick brown fox jumps over the lazy dog.                                                                  
After stripping a,e,i,o,u                                                                                     
Th qck brwn fx jmps vr th lzy dg.                             
'''