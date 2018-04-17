def test_range(n):
    if n in range(3,9):
        return True
    else :
        return False

if __name__=="__main__":
    n = int(input('xin moi nhap so'))
    print(test_range(n))
