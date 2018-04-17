'''Question: 
 Write a Python program to convert unix timestamp string to readable date.
'''

# Python code: 

import datetime
print(
    datetime.datetime.fromtimestamp(
        int("1284105682")
    ).strftime('%Y-%m-%d %H:%M:%S')
)


'''Output sample: 
2010-09-10 13:31:22 
'''