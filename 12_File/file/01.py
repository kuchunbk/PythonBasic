def file_read(fname):

        txt = open(fname)

        return (txt.read())

if __name__=="__main__":
    fname = 'E:\\Tu hocj\\abc.txt'
    print(file_read(fname))
