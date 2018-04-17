'''Question: 
Write a Python program to print next 5 days starting from today.
'''

# Python code: 


import datetime
base = datetime.datetime.today()
for x in range(0, 5):
      print(base + datetime.timedelta(days=x))
	  

'''Output sample: 
2017-05-06 12:27:53.632939                                                                                    
2017-05-07 12:27:53.632939                                                                                    
2017-05-08 12:27:53.632939                                                                                    
2017-05-09 12:27:53.632939                                                                                    
2017-05-10 12:27:53.632939  
'''