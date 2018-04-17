def remove_list(list1):
    set1=set(list1)
    list2 = list(set1)
    return list2

if __name__=="__main__":
    list1= [1,2,3,3,3,3,4,5]
    print(remove_list(list1))