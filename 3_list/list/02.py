def nhan_list(items):
    tich = 1
    for item in items :
        tich = tich * item
    return tich


if __name__ == "__main__":
    items =[1, 2, 4, 5, 6]
    print(nhan_list(items))