'''Question: 
Write a Python program to calculate the area of a sector.
Note: A circular sector or circle sector, is the portion of a disk enclosed by two radii and an arc, where the smaller area is known as the minor sector and the larger being the major sector.
'''

# Python code: 

def sectorarea():
    pi=22/7
    radius = float(input('Radius of Circle: '))
    angle = float(input('angle measure: '))
    if angle >= 360:
        print("Angle is not possible")
        return
    sur_area = (pi*radius**2) * (angle/360)
    print("Sector Area: ", sur_area)

sectorarea()


'''Output sample: 
Radius of Circle: 4                                                                                           
angle measure: 45                                                                                             
Sector Area:  6.285714285714286  
'''