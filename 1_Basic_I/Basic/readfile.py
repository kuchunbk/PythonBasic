def file_read_from_head(fname, nlines):

        from itertools import islice

        with open(fname) as f:

                for line in islice(f, nlines):

                        print(line)

file_read_from_head('E:\\Tu hocj\\abc.txt',4)

