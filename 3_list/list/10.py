def find_word(list1,n):
    for item in list1:
        if len(item) > n:
            print(item)

if __name__ == "__main__":
    n = int(input('xin moi nhap so'))
    list1 = ['lan anh','tran luan', 'mai thao', 'doi khong nhu mo']
    print(find_word(list1,n))