def creat_dict(n):
    d = dict()
    for x in range(1,n+1):
        d[x]=x*x
    return d

if __name__== "__main__":
    n=int(input("Input a number "))
    print(creat_dict(n))