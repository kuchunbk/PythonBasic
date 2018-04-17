'''Question: 
Write a Python program to find files and skip directories of a given directory.
'''

# Python code: 

import os
print([f for f in os.listdir('/home/students') if os.path.isfile(os.path.join('/home/students', f))])


'''Output sample: 
['test.txt', '.mysql_history', '.bash_logout', '.bash_history', '.profile', 'abc.py', '.viminfo', 'mynewtest.t
xt', 'myfile.txt', 'logging_example.out', '.web-term.json', 'abc.txt', '64a57280-272f-11e7-9ce4-832a8e030fef.p
y', 'exercise.cs', '.bashrc', 'Example.cs', 'myfig.png', 'file.out', 'line.gif', 'mmm.txt\n', 'temp.txt', 'ddd
d.txt\n', 'sss.dat\n', 'result.txt', 'output.jpg', '26492-1274250701.png', 'mytest.txt'] 
'''