def near_thousand(n):
    return ((abs(1000 - n) <= 100) or (abs(2000 - n) <= 100))

if __name__ == "__main__":
    n = int(input("xin moi nhap so"))
    print(near_thousand(n))