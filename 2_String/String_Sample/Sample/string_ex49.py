'''Question: 
Write a Python program to count and display the vowels of a given text.
'''

# Python code: 

def vowel(text):
    vowels = "aeiuoAEIOU"
    print(len([letter for letter in text if letter in vowels]))
    print([letter for letter in text if letter in vowels])
vowel('w3resource');


'''Output sample: 
4                                                                                                             
['e', 'o', 'u', 'e']               
'''