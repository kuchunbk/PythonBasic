def update_dict(dict,dict1,dict2):
    dict.update(dict1)
    dict.update(dict2)
    return dict

if __name__== "__main__":
    dict = {0: 10, 1: 20}
    dict1 = {3:30, 4:40}
    dict2 = {5:50,6:60}
    print(update_dict(dict,dict1,dict2))