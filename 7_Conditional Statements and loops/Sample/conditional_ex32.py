'''Question: 
Write a Python program to check whether an alphabet is a vowel or consonant.
'''

# Python code: 

l = input("Input a letter of the alphabet: ")

if l in ('a', 'e', 'i', 'o', 'u'):
	print("%s is a vowel." % l)
elif l == 'y':
	print("Sometimes letter y stand for vowel, sometimes stand for consonant.")
else:
	print("%s is a consonant." % l) 
	

'''Output sample: 
Input a letter of the alphabet: u                                                                             
u is a vowel. 
'''