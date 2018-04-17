import math

def convert(do):
    radian = do * math.pi / 180
    return radian

if __name__ =="__main__":
    do = float(input('xin moi nhap do'))
    print(convert(do))