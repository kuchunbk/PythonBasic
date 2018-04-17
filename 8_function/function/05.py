def calculate_n(n):
    if n < 0:
        return 'xin moi nhap lai so'
    elif n ==0:
        return '=1'
    else:
        giai_thua = 1
        for i in range(1,n+1):
            giai_thua = giai_thua * i
        return giai_thua
    
if __name__ =="__main__":
    n = int(input('xin moi nhap so'))
    print(calculate_n(n))
            