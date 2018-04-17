'''Question: 
 Write a Python program to convert seconds to day, hour, minutes and seconds.
'''

# Python code: 

time = float(input("Input time in seconds: "))
day = time // (24 * 3600)
time = time % (24 * 3600)
hour = time // 3600
time %= 3600
minutes = time // 60
time %= 60
seconds = time
print("d:h:m:s-> %d:%d:%d:%d" % (day, hour, minutes, seconds))


'''Output sample: 
Input time in seconds: 1234565                                                                                
d:h:m:s-> 14:6:56:5 
'''