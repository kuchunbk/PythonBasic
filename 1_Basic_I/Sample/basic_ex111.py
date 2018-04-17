'''Question: 
Write a Python program to make file lists from current directory using a wildcard.
'''

# Python code: 

import glob
file_list = glob.glob('*.*')
print(file_list)


'''Output sample: 
['30eb5e10-2675-11e7-a9c1-cf681af3cdf1.py', 'test.txt', 'abc.py', '
mynewtest.txt', 'myfile.txt', 'logging_example.out', '35ba4b40-2675
-11e7-a9c1-cf681af3cdf1.py', '30c8bae0-2675-11e7-a9c1-cf681af3cdf1.
py', 'abc.txt', 'exercise.cs', 'Example.cs', 'myfig.png', 'file.out
', 'line.gif', 'mmm.txt\n', 'temp.txt', 'dddd.txt\n', 'sss.dat\n', 
'result.txt', 'output.jpg', '26492-1274250701.png', 'mytest.txt']
'''