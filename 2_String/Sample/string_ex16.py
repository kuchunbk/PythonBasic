'''Question: 
Write a Python function to insert a string in the middle of a string.
'''

# Python code: 

def insert_sting_middle(str, word):
	return str[:2] + word + str[2:]

print(insert_sting_middle('[[]]', 'Python'))
print(insert_sting_middle('{{}}', 'PHP'))
print(insert_sting_middle('<<>>', 'HTML'))


'''Output sample: 
[[Python]]                                                                                                    
{{PHP}}                                                                                                       
<<HTML>> 
'''