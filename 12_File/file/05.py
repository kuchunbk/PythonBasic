def file_read(fname):
    with open(fname) as f:
    #Content_list is the list that contains the read lines.     

                content = f.readlines()

                print(content)



file_read('E:\\Tu hocj\\abc.txt')