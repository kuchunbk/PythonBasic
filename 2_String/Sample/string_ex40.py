'''Question: 
Write a Python program to reverse words in a string.
'''

# Python code: 

def reverse_string_words(text):
    for line in text.split('\n'):
        return(' '.join(line.split()[::-1]))
print(reverse_string_words("The quick brown fox jumps over the lazy dog."))
print(reverse_string_words("Python Exercises."))


'''Output sample: 
dog. lazy the over jumps fox brown quick The                                                                  
Exercises. Python
'''