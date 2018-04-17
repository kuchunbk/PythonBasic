'''Question: 
Write a Python program to convert all units of time into seconds.
'''

# Python code: 

days = int(input("Input days: ")) * 3600 * 24
hours = int(input("Input hours: ")) * 3600
minutes = int(input("Input minutes: ")) * 60
seconds = int(input("Input seconds: "))

time = days + hours + minutes + seconds

print("The  amounts of seconds", time)


'''Output sample: 
Input days: 4                                                                                                 
Input hours: 5                                                                                                
Input minutes: 20                                                                                             
Input seconds: 10                                                                                             
The  amounts of seconds 364810 
'''