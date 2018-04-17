def calculate_total(n1,n2,n3):
    if n1 == n2 and n2 == n3:
        return 3 *( n1+ n2+ n3)
    else:
        return n1+ n2+ n3

if __name__ == "__main__":
    n1= int(input('xin moi nhap so thu nhat'))
    n2= int(input('xin moi nhap so thu hai'))
    n3= int(input('xin moi nhap so thu ba'))
    print(calculate_total(n1,n2,n3))