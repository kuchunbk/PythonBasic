import math

def perimeter_circle(input_r):
    perimeter_circle = math.pi * input_r
    return perimeter_circle

if __name__ == "__main__":
    input_r = float(input(" xin moi nhap ban kinh"))
    print(perimeter_circle(input_r))