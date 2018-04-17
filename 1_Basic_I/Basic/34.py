def sum_tow(a,b):
    if a+ b <=20 and a+b >=15 :
        return 20
    else:
        return a+b
    
if __name__== "__main__":
    a=int(input('nhap a'))
    b= int(input('nhap b'))
    print(sum_tow(a,b))