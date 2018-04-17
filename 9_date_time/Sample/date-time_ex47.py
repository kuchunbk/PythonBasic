'''Question: 
Write a Python program display a list of the dates for the 2nd Saturday of every month for a given year.
'''

# Python code: 

import calendar
# Show every month
for month in range(1, 13):
    cal = calendar.monthcalendar(2020, month)
    first_week  = cal[0]
    second_week = cal[1]
    third_week  = cal[2]

    # If a Saturday presents in the first week, the second Saturday
    # is in the second week.  Otherwise, the second Saturday must 
    # be in the third week.
    
    if first_week[calendar.THURSDAY]:
        holi_day = second_week[calendar.THURSDAY]
    else:
        holi_day = third_week[calendar.THURSDAY]

    print('%3s: %2s' % (calendar.month_abbr[month], holi_day))
	

'''Output sample: 
Jan:  9                                                                                                       
Feb: 13                                                                                                       
Mar: 12                                                                                                       
Apr:  9                                                                                                       
May: 14                                                                                                       
Jun: 11                                                                                                       
Jul:  9                                                                                                       
Aug: 13                                                                                                       
Sep: 10                                                                                                       
Oct:  8                                                                                                       
Nov: 12                                                                                                       
Dec: 10   
'''