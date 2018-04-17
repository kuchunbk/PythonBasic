def remove_char(str1,str2,str3):
    return str1.replace( str2,str3)

if __name__ == "__main__":
    str1 = input('xin moi nhap chuoi')
    str2 = input('chuoi muon xoa bo')
    str3 = ''
    print('chuoi moi:',remove_char(str1,str2,str3))