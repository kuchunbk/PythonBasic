def  math(input_data):
    n1 = int( "%s" % a )
    n2 = int( "%s%s" % (a,a) )
    n3 = int( "%s%s%s" % (a,a,a) )
    return n1+ n2+ n3

if __name__ == "__main__":
    input_data = 5
    print(math(input_data))