def unique_list(list1):
    list2 = []
    for item in list1:
        if item not in list2:
            list2.append(item)
    return list2


if __name__=="__main__":
    list1 = [1,2,3,4,3,2,3,4,3]
    print(unique(list1))