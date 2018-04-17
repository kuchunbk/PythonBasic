def print_int_float(n):
    x = float(n)
    y = int(float(n))
    return x,y

if __name__=="__main__":
    n = 246.24424
    print(print_int_float(n))