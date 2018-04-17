'''Question: 
 Write a Python program to list all files in a directory in Python.
'''

# Python code: 

from os import listdir
from os.path import isfile, join
files_list = [f for f in listdir('/home/students') if isfile(join('/home/students', f))]
print(files_list);


'''Output sample: 
['3ff44d80-2423-11e7-807b-bd9de91b1602.py', 'f5272c90-2423-11e7-807b-bd9de91b1602.py', 'test.txt', 'f34e26d0-2
423-11e7-807b-bd9de91b1602.py', 'f6a62b70-2423-11e7-807b-bd9de91b1602.py', '.mysql_history', '.bash_logout', '
037db660-240b-11e7-807b-bd9de91b1602.py', '3d299190-241f-11e7-807b-bd9de91b1602.py', '8e7e22f0-240f-11e7-807b-
bd9de91b1602.py', '.bash_history', '276b1dd0-2404-11e7-807b-bd9de91b1602.py', '7e2f05d0-241a-11e7-807b-bd9de91
b1602.py', '6956ba40-2429-11e7-807b-bd9de91b1602.py', '.profile', 'abc.py', 'f69a4490-2423-11e7-807b-bd9de91b1
602.py', '.viminfo', 'mynewtest.txt', 'myfile.txt', 'logging_example.out', '.web-term.json', 'd2c942f0-2423-11
e7-807b-bd9de91b1602.py', 'ca7c2750-242a-11e7-807b-bd9de91b1602.py', 'abc.txt', 'exercise.cs', '.bashrc', 'Exa
mple.cs', '2f5aa190-2428-11e7-807b-bd9de91b1602.py', '2d5d6540-2418-11e7-807b-bd9de91b1602.py', '5bfc84e0-240d
-11e7-807b-bd9de91b1602.py', '940ca5b0-2406-11e7-807b-bd9de91b1602.py', 'myfig.png', 'file.out', 'a7af6660-241
6-11e7-807b-bd9de91b1602.py', '4a690da0-2428-11e7-807b-bd9de91b1602.py', 'line.gif', 'mmm.txt\n', 'temp.txt', 
'fb6e28e0-2425-11e7-807b-bd9de91b1602.py', 'f0896180-2423-11e7-807b-bd9de91b1602.py', 'dddd.txt\n', '700da350-
2413-11e7-807b-bd9de91b1602.py', 'sss.dat\n', '05f2fa20-2421-11e7-807b-bd9de91b1602.py', 'result.txt', '68c38d
e0-241c-11e7-807b-bd9de91b1602.py', 'output.jpg', 'c930d080-2407-11e7-807b-bd9de91b1602.py', '2e8ace70-2428-11
e7-807b-bd9de91b1602.py', '26492-1274250701.png', 'mytest.txt', '07fd1540-2411-11e7-807b-bd9de91b1602.py'] 
'''