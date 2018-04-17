
def remove_char(str1, n):
    first_part = str1[:n] 
    last_pasrt = str1[n+1:]
    return first_part + last_pasrt

if __name__ == "__main__":
    n= 2
    str1= 'tran van luan'
    print(remove_char(str1,n))