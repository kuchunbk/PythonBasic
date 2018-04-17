def add_number(a,b):
    if type(a) !=int or type(b) != int:
        return('khong phai la so nguyen')
    else:
        return a+ b
    
if __name__=="__main__":
    a= 5,4
    b= 5
    print(add_number(a,b))