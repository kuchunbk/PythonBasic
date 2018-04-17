def new_string(str):
    if len(str) >= 2 and str[:2] == 'Is':
        return str
    else :
        return 'Is' + str

if __name__ == "__main__":
    str = input('xin moi nhap chuoi')
    print(new_string(str))
    
