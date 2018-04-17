def lower(str1):
    return 'chuoi thuong',str1.lower() 

def upper(str1):
    return 'chuoi hoa',str1.upper()

if __name__ == "__main__":
    str1 = input('xin moi nhap chuoi')
    print(lower(str1))
    print(upper(str1))