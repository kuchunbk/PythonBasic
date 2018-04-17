def difference(n):
    if n <= 17:
        return 17 - n
    else:
        return (n - 17) * 2 

if __name__ == "__main__":
    n = int(input('xin moi nhap so'))
    print(difference(n))