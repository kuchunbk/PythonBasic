def  area_trapezoid(Height,first_value,second_value):
    area = (first_value + second_value) * Height / 2
    return area

if __name__=="__main__":
    Height = 5
    first_value = 5
    second_value = 6
    print(area_trapezoid(Height,first_value,second_value))
    
    