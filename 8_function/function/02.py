def sum_list(list1):
    sum_list = 0
    for item in list1:
        sum_list = sum_list + item
    return sum_list

if __name__=="__main__":
    list1 = (8, 2, 3, -1, 7)
    print(sum_list(list1))