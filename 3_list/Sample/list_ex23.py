'''Question: 
Write a Python program to flatten a shallow list.
'''

# Python code: 

import itertools
original_list = [[2,4,3],[1,5,6], [9], [7,9,0]]
new_merged_list = list(itertools.chain(*original_list))
print(new_merged_list)


'''Output sample: 
[2, 4, 3, 1, 5, 6, 9, 7, 9, 0] 
'''