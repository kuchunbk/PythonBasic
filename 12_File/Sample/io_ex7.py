'''Question: 
Write a Python program to read a file line by line store it into an array.
'''

# Python code: 


def file_read(fname):
        content_array = []
        with open(fname) as f:
                #Content_list is the list that contains the read lines.     
                for line in f:
                        content_array.append(line)
                print(content_array)

file_read('test.txt')


'''Output sample: 
['Welcome to w3resource.com.\n', 'Append this text.Append this text.Append this text.\n', 'Append this text.\n
', 'Append this text.\n', 'Append this text.\n', 'Append this text.\n']  
'''