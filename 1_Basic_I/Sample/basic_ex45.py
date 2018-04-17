'''Question: 
 Write a python program to call an external command in Python.
'''

# Python code: 

from subprocess import call
call(["ls", "-l"])


'''Output sample: 
drwxrwxr-x 2 students  students    4096 Sep 15  2016 c48d5200-7b43-11e6-b7e4-2516b8e1f7f8                     
drwxrwxr-x 2 students  students    4096 Sep 21  2016 c4a96850-7fdf-11e6-a2b3-172481646809                     
drwxrwxr-x 2 students  students    4096 Sep  7  2016 c4d98410-74de-11e6-ac36-65f2f75d0c7b                     
drwxrwxr-x 2 students  students    4096 Sep  6  2016 c4fa6e10-7424-11e6-812c-5574d751e2d7                     
drwxrwxr-x 2 prashanta prashanta   4096 Feb 20 18:24 c5216400-f76b-11e6-8ad1-9b7f6e755728   
-------
-rw-rw-r-- 1 students  students      27 Sep 28  2016 temp.txt                                                 
-rw-rw-r-- 1 students  students      27 Sep 28  2016 test.txt  
'''