'''Question: 
Write a Python program to split a list into different variables.
'''

# Python code: 

color = [("Black", "#000000", "rgb(0, 0, 0)"), ("Red", "#FF0000", "rgb(255, 0, 0)"),
         ("Yellow", "#FFFF00", "rgb(255, 255, 0)")]
var1, var2, var3 = color
print(var1)
print(var2)
print(var3)


'''Output sample: 
('Black', '#000000', 'rgb(0, 0, 0)')                                                                          
('Red', '#FF0000', 'rgb(255, 0, 0)')                                                                          
('Yellow', '#FFFF00', 'rgb(255, 255, 0)') 
'''