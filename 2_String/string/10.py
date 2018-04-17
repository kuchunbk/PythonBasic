def add_char(str1,str2,n):
    return str1[:n] + str2 + str1[n+1:]

if __name__ == "__main__":
    str1 = "tran van luan"
    str2 = "hai duong"
    n = 3
    print(add_char(str1,str2,n))