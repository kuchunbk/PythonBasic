def larger_str(str,n):
    result = ''
    for i in range(n):
        result = result + str
    return result

if __name__ == "__main__":
    str= input("xin moi nhap chuoi")
    n= int(input('xin moi nhap so lan ban sao'))
    print(larger_str(str,n))