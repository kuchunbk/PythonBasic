def common_data(list1,list2):
    for item1 in list1:
        for item2 in list2:
            if item1 == item2:
                return True


if __name__ == "__main__":
    list1 = [1,2,3,4,5]
    list2 = [6,7,8,5]
    print(common_data(list1,list2))
         