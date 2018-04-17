def max_three_number(x,y,z):
    if x> y and x> z:
        return x
    elif y > z and y > x:
        return y
    else:
        return z
    
if __name__=="__main__":
    x=6
    y=9
    z=32
    print(max_three_number(x,y,z))
            