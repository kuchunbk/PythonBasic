'''Question: 
Write a Python program to test whether a passed letter is a vowel or not.
'''

# Python code: 

def is_vowel(char):
    all_vowels = 'aeiou'
    return char in all_vowels
print(is_vowel('c'))
print(is_vowel('e'))


'''Output sample: 
False                                                                                                         
True 
'''