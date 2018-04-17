def update_dict(dict1,dict2):
    dict1.update(dict2)
    return dict1

if __name__ =="__main__":
    dict1 ={1:10, 2:20} 
    dict2 ={3:30, 4:40}
    print(update_dict(dict1,dict2))