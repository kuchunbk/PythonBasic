def count_string(str1):
    count= 0
    for char in str1 :
        count +=1
    return count


if __name__ =="__main__":
    str1 = "tran van luan"
    print(count_string(str1))