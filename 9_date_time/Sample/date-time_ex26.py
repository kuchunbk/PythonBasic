'''Question: 
Write a Python program calculates the date six months from the current date using the datetime module.
'''

# Python code: 

import datetime
print((datetime.date.today() + datetime.timedelta(6*365/12)).isoformat())


'''Output sample: 
2017-11-04
'''