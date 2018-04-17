def count_word(str1):
    return list(map(len,str1.split()))

if __name__ == "__main__":
    str1 = 'tran van luan'
    print(count_word(str1))