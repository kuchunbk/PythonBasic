'''Question: 
Write a Python program to calculate an age in year. 
'''

# Python code: 

from datetime import date

def calculate_age(dtob):
    today = date.today()
    return today.year - dtob.year - ((today.month, today.day) < (dtob.month, dtob.day))
print()
print(calculate_age(date(2006,10,12)))
print(calculate_age(date(1989,1,12)))
print()


'''Output sample: 
10                                                                                                            
28
'''