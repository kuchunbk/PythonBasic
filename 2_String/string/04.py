def change_char(str1):
    char = str1[0]
    length = len(str1)
    str1 = str1.replace(char, '$')
    str1 = char + str1[1:]
    return str1

if __name__ =="__main__":
    str1 = input('xin moi nhap chuoi')
    print(change_char(str1))