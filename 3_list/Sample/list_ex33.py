'''Question: 
Write a Python program to generate all sublists of a list.
'''

# Python code: 

def sub_lists(my_list):
	subs = [[]]
	for i in range(len(my_list)):
		n = i+1
		while n <= len(my_list):
			sub = my_list[i:n]
			subs.append(sub)
			n += 1
	
	return subs

l1 = [10, 20, 30, 40]
l2 = ['X', 'Y', 'Z']
print(sub_lists(l1))
print(sub_lists(l2))


'''Output sample: 

[[], [10], [10, 20], [10, 20, 30], [10, 20, 30, 40], [20], [20, 30], [20, 30, 40], [30], [30, 40], [40]]      
[[], ['X'], ['X', 'Y'], ['X', 'Y', 'Z'], ['Y'], ['Y', 'Z'], ['Z']] 
'''