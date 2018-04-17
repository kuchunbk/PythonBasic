def add_string(str1):
    length = len(str1)
    if length > 2:
        if str1[-3:] == 'ing':
            str1 += 'ly'
        else:
            str1 += 'ing'
        return str1
    else:
        return 'xin moi nhap lai chuoi'

if __name__ == "__main__":
    str1= input('xin moi nhap chuoi')
    print(add_string(str1))
