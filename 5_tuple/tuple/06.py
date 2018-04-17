def convert_tuple_to_string(tuple1):
    string= ''.join((tuple1))
    return string

if __name__=="__main__":
    tuple1= ('a', 'b', 'c', 'd', 'g', 'x', 'r', 'e')
    print(convert_tuple_to_string(tuple1))