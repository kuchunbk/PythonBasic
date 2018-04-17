def combine_each_line(file1,file2):
    with open(file1) as my_file1:
        with open(file2) as my_file2:
            for line1, line2 in zip(my_file1,my_file2):
                print(line1 + line2)

if __name__=="__main__":
    file1 = 'E:\\T? H?c\\python\\abc.txt'
    file2 = 'E:\\T? H?c\\python\\test.txt'
    print(combine_each_line(file1,file2))