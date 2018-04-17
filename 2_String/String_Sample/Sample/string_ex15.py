'''Question: 
Write a Python function to create the HTML string with tags around the word(s).
Sample function and result : 
add_tags('i', 'Python') -> '<i>Python</i>'
add_tags('b', 'Python Tutorial') -> '<b>Python Tutorial </b>'
'''

# Python code: 

def add_tags(tag, word):
	return "<%s>%s" % (tag, word, tag)
print(add_tags('i', 'Python'))
print(add_tags('b', 'Python Tutorial'))


'''Output sample: 
Python                                                                                                 
Python Tutorial 
'''