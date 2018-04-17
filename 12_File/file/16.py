def check_file_open(file_name):
    my_file = open(file_name)
    return ('file dang mo')

def check_file_close(file_name):
    my_file = open(file_name)
    my_file.close()
    return ("file dang dong",my_file.closed)

if __name__=="__main__":
    file_name = 'E:\\T? H?c\\python\\test.txt'
    print(check_file_open(file_name))
    print(check_file_close(file_name))