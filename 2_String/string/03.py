def cut_string(str1):
    if len(str1) < 2:
        return ""
    else:
        return str1[0:2] + str1[-2:]
    
if __name__ == "__main__":
    str1= input('xin moi nhap chuoi')
    print(cut_string(str1))