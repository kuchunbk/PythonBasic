'''Question: 
Write a Python program that accepts a word from the user and reverse it.
'''

# Python code: 

word = input("Input a word to reverse: ")

for char in range(len(word) - 1, -1, -1):
  print(word[char], end="")
print("\n")


'''Output sample: 
Input a word to reverse: ecruoser3w  
w3resource
'''