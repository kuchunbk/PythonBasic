'''Question: 
Write a Python program to print the index of the character in a string.
'''

# Python code: 

str1 = "w3resource"
for index, char in enumerate(str1):
    print("Current character", char, "position at", index )


'''Output sample: 
Current character w position at 0                                                                             
Current character 3 position at 1                                                                             
Current character r position at 2                                                                             
Current character e position at 3                                                                             
Current character s position at 4                                                                             
Current character o position at 5                                                                             
Current character u position at 6                                                                             
Current character r position at 7                                                                             
Current character c position at 8                                                                             
Current character e position at 9 
'''