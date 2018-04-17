# có 2 cách ð? thêm ph?n t? vào ki?u d? li?u tuple
#chuy?n v? list r?i app
# thêm vào ki?u tuple
# th?m theo ki?u công

def add_tuple(tuplex):
    tuplex1= tuplex +(5,)
    return tuplex1

def add_tuple2(tuplex):
    listx= list(tuplex)
    listx.append(30)
    tuplex2 =tuple(listx)
    return tuplex2


if __name__=="__main__":
    tuplex = (4, 6, 2, 8, 3, 1) 
    print(add_tuple(tuplex))
    print(add_tuple2(tuplex))
