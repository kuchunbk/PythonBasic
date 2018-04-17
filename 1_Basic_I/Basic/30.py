import math
def acreage(a,b,c):
    p= (a+ b+ c) /2
    return math.sqrt((p-a)*(p-b)*(p-c)*p)

if __name__ == "__main__":
    a = int(input('xin moi nhap canh thu 1 cua tam giac'))
    b = int(input('xin moi nhap canh thu 2 cua tam giac'))
    c = int(input('xin moi nhap canh thu 3 cua tam giac'))
    print(acreage(a,b,c))