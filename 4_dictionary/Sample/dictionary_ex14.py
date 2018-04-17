'''Question: 
Write a Python program to sort a dictionary by key.
'''

# Python code: 

color_dict = {'red':'#FF0000',
          'green':'#008000',
          'black':'#000000',
          'white':'#FFFFFF'}

for key in sorted(color_dict):
    print("%s: %s" % (key, color_dict[key]))
	

'''Output sample: 
black: #000000                                                                                                
green: #008000                                                                                                
red: #FF0000                                                                                                  
white: #FFFFFF 
'''