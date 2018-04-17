def sum_there(a,b,c):
    if a== b or b== c or c== a:
        return 0
    else: 
        return a+ b+ c

if __name__ == "__main__":
    a= int(input('xin moi nhap a'))
    b= int(input('xin moi nhap b'))
    c= int(input('xin moi nhap c'))
    print(sum_there(a,b,c))