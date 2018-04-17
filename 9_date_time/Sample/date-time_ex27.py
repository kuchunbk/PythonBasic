'''Question: 
Write a Python program to create 12 fixed dates from a specified date over a given period. The difference between two dates will be 20. 
'''

# Python code: 

import datetime
def every_20_days(date):
    print('Starting Date: {d}'.format(d=date))
    print("Next 12 days :")
    for _ in range(12):
        date=date+datetime.timedelta(days=20)
        print('{d}'.format(d=date))

dt = datetime.date(2016,8,1)
every_20_days(dt)


'''Output sample: 
Starting Date: 2016-08-01                                                                                     
Next 12 days :                                                                                                
2016-08-21                                                                                                    
2016-09-10                                                                                                    
2016-09-30                                                                                                    
2016-10-20                                                                                                    
2016-11-09                                                                                                    
2016-11-29                                                                                                    
2016-12-19                                                                                                    
2017-01-08                                                                                                    
2017-01-28                                                                                                    
2017-02-17                                                                                                    
2017-03-09                                                                                                    
2017-03-29                 
'''