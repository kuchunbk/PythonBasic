import math

def convert_radian_degree(radian):
    degree = radian * 180 / math.pi
    return degree

if __name__=="__main__":
    radian = float(input('xin moi nhap radian'))
    print(convert_radian_degree(radian))