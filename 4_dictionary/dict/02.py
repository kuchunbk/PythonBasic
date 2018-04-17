def update_dict(dict,dict2):
    dict.update(dict2)
    return dict

if __name__== "__main__":
    dict = {0: 10, 1: 20}
    dict2 = {2: 30}
    print(update_dict(dict,dict2))