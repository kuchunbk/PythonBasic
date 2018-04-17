def frequency_char(str1):
    dict = {}
    for char in str1:
        keys = dict.keys()
        if char in keys:
            dict[char] += 1
        else:
            dict[char]= 1
    return dict

if __name__ == "__main__":
    str1 = input('xin moi nhap chuoi')
    print(frequency_char(str1))