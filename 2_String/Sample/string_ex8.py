'''Question: 
Write a Python function that takes a list of words and returns the length of the longest one.
'''

# Python code: 

def find_longest_word(words_list):
    word_len = []
    for n in words_list:
        word_len.append((len(n), n))
    word_len.sort()
    return word_len[-1][1]

print(find_longest_word(["PHP", "Exercises", "Backend"]))


'''Output sample: 
Exercises
'''