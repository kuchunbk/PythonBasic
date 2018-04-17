def file_read_from_head(fname,nlines):
    from itertools import islice
    with open(fname) as my_file:
        for line in islice(my_file, nlines):
            print (line)

print(file_read_from_head('E:\\Tu hocj\\abc.txt',5))
