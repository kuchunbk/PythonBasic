def file_read(fname):
        with open (fname, "r") as myfile:
                data=myfile.readlines()# luu vao 1 bien
                print(data)
file_read('test.txt')
