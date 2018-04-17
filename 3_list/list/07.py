def remove_duplicates(data):
    set1= set() # tao 1 set dua vao mac dinh set khong chua cac phan tu trung nhau
    for item in data:
        set1.add(item)
    return set1

if __name__ == "__main__":
    data = [10,20,30,20,10,50,60,40,80,50,40]
    print(remove_duplicates(data))